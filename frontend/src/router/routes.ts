import { RouteRecordRaw } from 'vue-router';

// Import layouts
const MainLayout = () => import('layouts/MainLayout.vue');

// Import pages
const ChatPage = () => import('pages/ChatPage.vue');

// List route names
export enum PageName {
  chat = 'chat',
}

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: MainLayout,
    children: [{ name: PageName.chat, path: '', component: ChatPage }],
  },

  // Unknown route
  {
    path: '/:catchAll(.*)*',
    redirect: { name: PageName.chat, params: {} },
  },
];

export default routes;
