<template>
  <q-btn v-bind="$props" class="a-btn" />
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { colors } from 'quasar';
import type { ABtnProps } from './baseComponents';

// Define props
const props = withDefaults(defineProps<ABtnProps>(), {
  padding: 'sm',
});

// Get outline color
const outlineHexColor = computed(() =>
  props.outlineColor ? colors.getPaletteColor(props.outlineColor) : undefined,
);
</script>

<style scoped lang="scss">
.a-btn.q-btn--outline:before {
  color: v-bind('outlineHexColor');
}
</style>
