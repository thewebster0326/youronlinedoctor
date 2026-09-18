/* Your Online Doctor - hero network scene.

   A patient node connecting outward to healthcare professional nodes, which
   connect onward to service nodes. Pulses travel the connections. This is the
   ecosystem diagram from the brief, rendered as the hero.

   Degrades to the CSS gradient underneath if Three.js is unavailable, if the
   visitor prefers reduced motion, or if WebGL is not supported. */

(function () {
  'use strict';

  var canvas = document.getElementById('network-canvas');
  if (!canvas) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (typeof window.THREE === 'undefined') return;

  var GOLD = 0xe6b64c;
  var GOLD_LIGHT = 0xf9e3a4;
  var CYAN = 0x5fd4e4;

  var isSmall = window.innerWidth < 760;

  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({
      canvas: canvas,
      alpha: true,
      antialias: !isSmall,
      powerPreference: 'low-power'
    });
  } catch (err) {
    return; // no WebGL - the CSS fallback stays visible
  }

  renderer.setClearColor(0x000000, 0);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, isSmall ? 1.5 : 1.8));

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(46, 1, 0.1, 100);
  camera.position.set(0, 0, 10.2);

  var group = new THREE.Group();
  // Sit the graph right of centre so it clears the headline on wide screens.
  group.position.x = isSmall ? 0 : 1.9;
  group.position.y = isSmall ? 1.4 : 0;
  group.rotation.x = -0.2;
  scene.add(group);

  /* ------------------------------------------------ node sprite texture */

  function discTexture() {
    var size = 64;
    var c = document.createElement('canvas');
    c.width = c.height = size;
    var ctx = c.getContext('2d');
    var grad = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
    grad.addColorStop(0, 'rgba(255,255,255,1)');
    grad.addColorStop(0.28, 'rgba(255,255,255,0.92)');
    grad.addColorStop(0.55, 'rgba(255,255,255,0.22)');
    grad.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, size, size);
    var tex = new THREE.Texture(c);
    tex.needsUpdate = true;
    return tex;
  }

  var sprite = discTexture();

  /* ------------------------------------------------------ graph topology */

  var PRO_COUNT = isSmall ? 6 : 7;   // GPs, specialists, psychologists, dietitians...
  var SVC_COUNT = isSmall ? 9 : 13;  // pharmacies, laboratories, diagnostics...

  var hub = new THREE.Vector3(0, 0, 0);
  var pros = [];
  var svcs = [];

  var i, angle, radius;

  for (i = 0; i < PRO_COUNT; i++) {
    angle = (i / PRO_COUNT) * Math.PI * 2 + 0.35;
    radius = 2.5;
    pros.push(new THREE.Vector3(
      Math.cos(angle) * radius,
      Math.sin(angle) * radius * 0.78,
      Math.sin(angle * 2.1) * 0.9
    ));
  }

  for (i = 0; i < SVC_COUNT; i++) {
    angle = (i / SVC_COUNT) * Math.PI * 2 + 0.12;
    radius = 4.5 + (i % 3) * 0.42;
    svcs.push(new THREE.Vector3(
      Math.cos(angle) * radius,
      Math.sin(angle) * radius * 0.74,
      Math.cos(angle * 1.7) * 1.5
    ));
  }

  /* ------------------------------------------------------------- edges */

  var edges = [];  // {a, b, tint}

  for (i = 0; i < pros.length; i++) {
    edges.push({ a: hub, b: pros[i], tint: 'gold' });
  }
  for (i = 0; i < svcs.length; i++) {
    // Each service attaches to its nearest two professionals.
    var nearest = pros
      .map(function (p, idx) { return { idx: idx, d: p.distanceTo(svcs[i]) }; })
      .sort(function (x, y) { return x.d - y.d; })
      .slice(0, 2);
    for (var n = 0; n < nearest.length; n++) {
      edges.push({ a: pros[nearest[n].idx], b: svcs[i], tint: 'cyan' });
    }
  }

  var linePos = new Float32Array(edges.length * 6);
  var lineCol = new Float32Array(edges.length * 6);
  var gold = new THREE.Color(GOLD);
  var cyan = new THREE.Color(CYAN);

  for (i = 0; i < edges.length; i++) {
    var e = edges[i];
    linePos[i * 6 + 0] = e.a.x; linePos[i * 6 + 1] = e.a.y; linePos[i * 6 + 2] = e.a.z;
    linePos[i * 6 + 3] = e.b.x; linePos[i * 6 + 4] = e.b.y; linePos[i * 6 + 5] = e.b.z;

    var col = e.tint === 'gold' ? gold : cyan;
    var nearAlpha = e.tint === 'gold' ? 1.0 : 0.62;
    var farAlpha = e.tint === 'gold' ? 0.45 : 0.2;
    lineCol[i * 6 + 0] = col.r * nearAlpha;
    lineCol[i * 6 + 1] = col.g * nearAlpha;
    lineCol[i * 6 + 2] = col.b * nearAlpha;
    lineCol[i * 6 + 3] = col.r * farAlpha;
    lineCol[i * 6 + 4] = col.g * farAlpha;
    lineCol[i * 6 + 5] = col.b * farAlpha;
  }

  var lineGeo = new THREE.BufferGeometry();
  lineGeo.setAttribute('position', new THREE.BufferAttribute(linePos, 3));
  lineGeo.setAttribute('color', new THREE.BufferAttribute(lineCol, 3));
  group.add(new THREE.LineSegments(lineGeo, new THREE.LineBasicMaterial({
    vertexColors: true,
    transparent: true,
    opacity: 0.95,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  })));

  /* ------------------------------------------------------------- nodes */

  function pointCloud(vectors, color, size, opacity) {
    var pos = new Float32Array(vectors.length * 3);
    for (var k = 0; k < vectors.length; k++) {
      pos[k * 3] = vectors[k].x;
      pos[k * 3 + 1] = vectors[k].y;
      pos[k * 3 + 2] = vectors[k].z;
    }
    var geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    var mat = new THREE.PointsMaterial({
      color: color,
      size: size,
      map: sprite,
      transparent: true,
      opacity: opacity,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      sizeAttenuation: true
    });
    var pts = new THREE.Points(geo, mat);
    group.add(pts);
    return pts;
  }

  var hubNode = pointCloud([hub], GOLD_LIGHT, 2.1, 1);
  pointCloud(pros, GOLD, 0.95, 1);
  pointCloud(svcs, CYAN, 0.55, 0.85);

  /* ------------------------------------------------------------ pulses */

  var PULSES = edges.length;
  var pulsePos = new Float32Array(PULSES * 3);
  var pulseGeo = new THREE.BufferGeometry();
  pulseGeo.setAttribute('position', new THREE.BufferAttribute(pulsePos, 3));

  var pulseMat = new THREE.PointsMaterial({
    color: GOLD_LIGHT,
    size: 0.4,
    map: sprite,
    transparent: true,
    opacity: 0.9,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    sizeAttenuation: true
  });
  group.add(new THREE.Points(pulseGeo, pulseMat));

  var travel = [];
  for (i = 0; i < PULSES; i++) {
    travel.push({ t: Math.random(), speed: 0.11 + Math.random() * 0.16 });
  }

  /* ------------------------------------------------------------- resize */

  function resize() {
    var w = canvas.clientWidth || window.innerWidth;
    var h = canvas.clientHeight || window.innerHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }

  window.addEventListener('resize', resize);
  resize();

  /* ------------------------------------------------------------ pointer */

  var targetX = 0, targetY = 0, curX = 0, curY = 0;

  if (!isSmall) {
    window.addEventListener('pointermove', function (e) {
      targetX = (e.clientX / window.innerWidth - 0.5) * 0.36;
      targetY = (e.clientY / window.innerHeight - 0.5) * 0.24;
    }, { passive: true });
  }

  /* ------------------------------------------------ run only when visible */

  var visible = true;
  var hero = canvas.parentNode;

  if ('IntersectionObserver' in window && hero) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
    }, { threshold: 0.02 }).observe(hero);
  }

  document.addEventListener('visibilitychange', function () {
    if (!document.hidden) clock = performance.now();
  });

  /* -------------------------------------------------------------- loop */

  var clock = performance.now();
  var elapsed = 0;

  function frame(now) {
    requestAnimationFrame(frame);

    var dt = Math.min((now - clock) / 1000, 0.05);
    clock = now;

    if (!visible || document.hidden) return;

    elapsed += dt;

    group.rotation.y += dt * 0.085;

    curX += (targetX - curX) * 0.045;
    curY += (targetY - curY) * 0.045;
    group.rotation.z = curX * 0.22;
    camera.position.x = -curX * 1.6;
    camera.position.y = curY * 1.2;
    camera.lookAt(group.position.x * 0.32, 0, 0);

    // Hub breathes gently so the centre reads as the active node.
    hubNode.material.size = 2.1 + Math.sin(elapsed * 1.5) * 0.22;

    for (var p = 0; p < PULSES; p++) {
      var tr = travel[p];
      tr.t += dt * tr.speed;
      if (tr.t > 1) tr.t -= 1;

      var edge = edges[p];
      var eased = tr.t * tr.t * (3 - 2 * tr.t);
      pulsePos[p * 3] = edge.a.x + (edge.b.x - edge.a.x) * eased;
      pulsePos[p * 3 + 1] = edge.a.y + (edge.b.y - edge.a.y) * eased;
      pulsePos[p * 3 + 2] = edge.a.z + (edge.b.z - edge.a.z) * eased;
    }
    pulseGeo.attributes.position.needsUpdate = true;

    renderer.render(scene, camera);
  }

  requestAnimationFrame(frame);
  canvas.classList.add('is-ready');
})();
