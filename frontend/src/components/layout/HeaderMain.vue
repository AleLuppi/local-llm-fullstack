<template>
  <q-header v-bind="$props" v-model="modelValue" :class="bgColor ? `bg-${bgColor}` : ''">
    <bar-windowed v-if="showWindowBar" :class="barColor ? `bg-${barColor}` : ''" />
  </q-header>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { QHeaderProps } from 'quasar';
import BarWindowed from 'components/layout/BarWindowed.vue';

// Define props
defineProps<
  Omit<QHeaderProps, 'modelValue'> & {
    // header background color
    bgColor?: string;

    // color of the main utility bar
    barColor?: string;
  }
>();

// Define model
const modelValue = defineModel<QHeaderProps['modelValue']>({ default: true });

// Should display utility bar
const showWindowBar = computed(() => process.env.MODE === 'electron');
</script>
