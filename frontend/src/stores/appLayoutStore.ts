/**
 * Store useful layout info and provide helpers to update them.
 */

import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useAppLayoutStore = defineStore('appLayout', () => {
  // Left drawer status
  const leftDrawerOpen = ref(false);

  // Right drawer status
  const rightDrawerOpen = ref(false);

  /**
   * Toggle the left drawer.
   */
  function toggleLeftDrawer() {
    leftDrawerOpen.value = !leftDrawerOpen.value;
  }

  /**
   * Set left drawer status.
   */
  function setLeftDrawer(value: boolean) {
    leftDrawerOpen.value = value;
  }

  /**
   * Toggle the right drawer.
   */
  function toggleRightDrawer() {
    rightDrawerOpen.value = !rightDrawerOpen.value;
  }

  /**
   * Set right drawer status.
   */
  function setRightDrawer(value: boolean) {
    rightDrawerOpen.value = value;
  }

  function $reset() {
    leftDrawerOpen.value = false;
    rightDrawerOpen.value = false;
  }

  return {
    leftDrawerOpen,
    rightDrawerOpen,
    toggleLeftDrawer,
    setLeftDrawer,
    toggleRightDrawer,
    setRightDrawer,
    $reset,
  };
});
