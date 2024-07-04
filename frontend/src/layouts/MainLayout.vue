<template>
  <q-layout view="hHh LpR fFf">
    <header-main bar-color="primary-dark" />

    <drawer-chat-history v-model="leftDrawerOpen" show-if-above bordered />

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue';
import HeaderMain from 'components/layout/HeaderMain.vue';
import { useDrawers } from 'src/composables/drawers';

// Import components
const DrawerChatHistory = defineAsyncComponent(
  () => import('components/layout/DrawerChatHistory.vue'),
);

// Drawer status
const { leftDrawerOpen } = useDrawers();
</script>
