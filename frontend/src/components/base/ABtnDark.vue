<template>
  <q-btn
    v-bind="$props"
    :icon="isDark ? fasMoon : fasSun"
    class="a-btn-dark"
    @click="isDark = !isDark"
  />
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { colors, useQuasar } from 'quasar';
import type { QBtnProps } from 'quasar';
import { fasMoon, fasSun } from '@quasar/extras/fontawesome-v6';

// Define props
const props = defineProps<
  Omit<QBtnProps, 'icon'> & { outlineColor?: string }
>();

// Init plugin
const $q = useQuasar();

// Set dark mode
const isDark = computed({
  get: () => $q.dark.isActive,
  set: (val) => $q.dark.set(val),
});

// Get outline color
const outlineHexColor = computed(() =>
  props.outlineColor ? colors.getPaletteColor(props.outlineColor) : undefined,
);
</script>

<style scoped lang="scss">
.a-btn-dark.q-btn--outline:before {
  color: v-bind('outlineHexColor');
}
</style>
