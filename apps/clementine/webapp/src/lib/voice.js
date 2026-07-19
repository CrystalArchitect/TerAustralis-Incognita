/** Local voice via the browser's speech synthesis — nothing leaves the machine. */

const supported = typeof window !== 'undefined' && 'speechSynthesis' in window;

export function voiceSupported() {
  return supported;
}

export function listVoices() {
  return supported ? window.speechSynthesis.getVoices() : [];
}

export function onVoicesChanged(cb) {
  if (supported) window.speechSynthesis.addEventListener('voiceschanged', cb);
}

export function speak(text, voiceName = '') {
  if (!supported) return;
  const clean = text.replace(/\s+/g, ' ').trim();
  if (!clean) return;
  const u = new SpeechSynthesisUtterance(clean);
  const v = listVoices().find((x) => x.name === voiceName);
  if (v) u.voice = v;
  window.speechSynthesis.speak(u);
}

export function stopSpeaking() {
  if (supported) window.speechSynthesis.cancel();
}
