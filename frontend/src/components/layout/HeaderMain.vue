<template>
  <q-header v-bind="$props" v-model="modelValue">
    <q-toolbar>
      <q-btn
        v-if="leftDrawerOpen != undefined"
        flat
        dense
        round
        icon="menu"
        aria-label="Menu"
        @click="leftDrawerOpen = !leftDrawerOpen"
      />

      <q-toolbar-title>{{ appName }}</q-toolbar-title>

      <div>v{{ appVersion }}</div>

      <q-btn
        v-if="rightDrawerOpen != undefined"
        flat
        dense
        round
        icon="menu"
        aria-label="Menu"
        @click="rightDrawerOpen = !rightDrawerOpen"
      />
    </q-toolbar>
  </q-header>
</template>

<script setup lang="ts">
import type { QHeaderProps } from 'quasar';

// Define props
withDefaults(defineProps<QHeaderProps>(), {});

// Define model
const modelValue = defineModel<QHeaderProps['modelValue']>({ default: true });
const leftDrawerOpen = defineModel<boolean>('leftDrawerOpen', {
  default: undefined,
});
const rightDrawerOpen = defineModel<boolean>('rightDrawerOpen', {
  default: undefined,
});

// Get app name and version
const appName = import.meta.env.VITE_APP_NAME;
const appVersion = import.meta.env.VITE_APP_VERSION;
</script>
