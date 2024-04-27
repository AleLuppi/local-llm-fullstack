<template>
  <a-btn
    v-bind="$props"
    :icon="isDark ? fasMoon : fasSun"
    @click="isDark = !isDark"
  />
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useQuasar } from 'quasar';
import type { ABtnDarkProps } from './baseComponents';
import { fasMoon, fasSun } from '@quasar/extras/fontawesome-v6';

// Define props
defineProps<ABtnDarkProps>();

// Init plugin
const $q = useQuasar();

// Set dark mode
const isDark = computed({
  get: () => $q.dark.isActive,
  set: (val) => $q.dark.set(val),
});
</script>
