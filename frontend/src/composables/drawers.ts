import { watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useAppLayoutStore } from 'src/stores/appLayoutStore';

export function useDrawers() {
  const { leftDrawerOpen, rightDrawerOpen } = storeToRefs(useAppLayoutStore());

  return {
    leftDrawerOpen,
    rightDrawerOpen,
  };
}
