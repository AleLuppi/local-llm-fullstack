/**
 * Store all user chats and provide helpers to update them.
 */

import { defineStore } from 'pinia';
import { ref, watch } from 'vue';
import type { Chat } from 'src/models/chat';
import { getChats } from 'src/api/apiAgent';

export const useChatHistoryStore = defineStore('chatHistory', () => {
  // All chats created by current user
  const chats = ref<{ [key: Chat['uid']]: Chat }>({});

  // Sorted chats by last update
  const dateSortedChats = ref<Chat[]>([]);
  watch(chats, () => (dateSortedChats.value = sortChatsByLastUpdate()), {
    immediate: true,
    deep: true,
  });

  /**
   * Sort current chat history by last update date.
   *
   * @returns {Chat[]} The sorted chat history.
   */
  function sortChatsByLastUpdate() {
    return Object.values(chats.value).sort(
      (a: Chat, b: Chat) => b.lastUpdate.getTime() - a.lastUpdate.getTime(),
    );
  }

  /**
   * Load chats from the API and add them to the chat history store.
   *
   * @param {boolean} [reset=false] - Whether to reset the chat history store.
   * @param {number} [retry=0] - How many times to retry loading chats upon error; use -1 to retry indefinitely.
   * @returns {Promise<typeof chats.value>} The updated chat history.
   */
  function loadChats(reset = false, retry = 0): Promise<typeof chats.value> {
    if (reset) $reset();
    return getChats()
      .then((historyChats) => {
        historyChats.forEach(addChat);
        return chats.value;
      })
      .catch(() => {
        if (retry) return loadChats(reset, retry - 1);
        return chats.value;
      });
  }

  /**
   * Get chat by ID.
   *
   * @param {string} chatId - ID of the chat to retrieve.
   * @returns {Chat} The chat with the given ID.
   */
  function getChat(chatId: string): Chat | undefined {
    return chats.value[chatId];
  }

  /**
   * Add a new chat to the store.
   *
   * @param {Chat} chat - The chat to add.
   * @returns {Chat} The newly added chat.
   */
  function addChat(chat: Chat): Chat {
    chats.value[chat.uid] = chat;
    return chat;
  }

  /**
   * Update an existing chat in the store.
   *
   * @param {Chat} chat - The chat to update.
   * @returns {Chat} The chat that has been replaced.
   */
  function updateChat(chat: Chat): Chat | undefined {
    const currentChat = getChat(chat.uid);
    chats.value[chat.uid] = chat;
    return currentChat;
  }

  /**
   * Delete a chat from the store.
   *
   * @param {Chat} chat - The chat to delete.
   * @returns {Chat} The deleted chat.
   */
  function deleteChat(chat: Chat | string): Chat | undefined {
    const currentChat = getChat(typeof chat === 'string' ? chat : chat.uid);
    if (currentChat) delete chats.value[currentChat.uid];
    return currentChat;
  }

  function $reset() {
    chats.value = {};
  }

  return {
    chats,
    dateSortedChats,
    loadChats,
    getChat,
    addChat,
    updateChat,
    deleteChat,
    $reset,
  };
});
