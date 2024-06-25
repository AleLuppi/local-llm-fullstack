<template>
  <q-layout view="hHh LpR fFf">
    <header-main
      v-model:left-drawer-open="leftDrawerOpen"
      bar-color="primary-dark"
    />

    <drawer-chat-history v-model="leftDrawerOpen" show-if-above bordered />

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import HeaderMain from 'components/layout/HeaderMain.vue';
import DrawerChatHistory from 'components/layout/DrawerChatHistory.vue';

// Drawer status
const leftDrawerOpen = ref(false);
</script>
