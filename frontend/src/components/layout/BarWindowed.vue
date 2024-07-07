<template>
  <q-bar class="q-electron-drag">
    <!-- Display slots -->
    <slot v-for="(_, slot) in $slots" :name="slot"></slot>

    <q-space />

    <!-- Utility buttons -->
    <q-btn v-if="!hideMinimize" dense flat icon="minimize" @click="minimize" />
    <q-btn
      v-if="!hideMaximize"
      dense
      flat
      icon="crop_square"
      @click="toggleMaximize"
    />
    <q-btn
      v-if="!hideClose"
      dense
      flat
      icon="close"
      class="btn-close"
      @click="closeApp"
    />
  </q-bar>
</template>

<script setup lang="ts">
import { useWindowApi } from 'src/composables/windowApi';

defineProps<{
  // whether to hide the minimize button
  hideMinimize?: boolean;

  // whether to hide the maximize / toggle button
  hideMaximize?: boolean;

  // whether to hide the close button
  hideClose?: boolean;
}>();

const { minimize, toggleMaximize, closeApp } = useWindowApi();
</script>

<style scoped lang="scss">
.btn-close {
  &:hover {
    background: $negative;
  }
}
</style>
