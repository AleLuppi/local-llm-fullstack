<template>
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

    <q-toolbar-title :class="{ 'text-grey': !agentConnected }">
      <span class="q-px-sm" style="font-size: medium">
        {{
          agentConnected
            ? $t('chat.agent.connected')
            : $t('chat.agent.disconnected')
        }}
      </span>
      <q-circular-progress
        v-if="!agentConnected"
        indeterminate
        rounded
        color="primary"
        :thickness="0.3"
        class="q-mx-sm"
      />
    </q-toolbar-title>

    <div>{{ $t('app.apiVersion') }}{{ appVersion }}</div>
  </q-toolbar>
</template>

<script setup lang="ts">
import { useAgentStatus } from 'src/composables/agentStatus';
import { useDrawers } from 'src/composables/drawers';

const { leftDrawerOpen } = useDrawers();

// Get app name and version
const appName = import.meta.env.VITE_APP_NAME;
const appVersion = import.meta.env.VITE_APP_VERSION;

// Check agent status
const { agentConnected } = useAgentStatus();
</script>
