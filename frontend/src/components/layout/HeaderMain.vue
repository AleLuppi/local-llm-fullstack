<template>
  <q-header v-bind="$props" v-model="modelValue">
    <bar-windowed v-if="showBar" />
  </q-header>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { QHeaderProps } from 'quasar';
import BarWindowed from 'components/layout/BarWindowed.vue';

// Define props
defineProps<QHeaderProps>();

// Define model
const modelValue = defineModel<QHeaderProps['modelValue']>({ default: true });

// Should display utility bar
const showBar = computed(() => process.env.MODE === 'electron');
</script>
