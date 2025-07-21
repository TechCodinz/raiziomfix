export const cloneMemory = {};

export function updateMemory(clone, topic, value) {
  if (!cloneMemory[clone]) cloneMemory[clone] = {};
  if (!cloneMemory[clone][topic]) cloneMemory[clone][topic] = 0;

  // Only update if new value is higher
  if (value > cloneMemory[clone][topic]) {
    cloneMemory[clone][topic] = value;
  }
}

export function getMemory(clone) {
  return cloneMemory[clone] || {};
}
