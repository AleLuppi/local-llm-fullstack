import { apiAgent } from 'src/boot/axios';
import { Chat } from 'src/models/chat';
import { ChatProps } from 'src/models/chatInterface';

/**
 * Get LLM agent health information.
 *
 * @returns {Promise<{ status: string }>} LLM agent status.
 */
export function getHealth(): Promise<{ status: string }> {
  return apiAgent.get('/health');
}

/**
 * Converts chat data from API into a Chat object.
 *
 * @param {Omit<ChatProps, 'uid'> & { id: string }} data - The API data to convert.
 * @returns {Chat} The Chat object created from the API data.
 */
function apiDataToChat(data: Omit<ChatProps, 'uid'> & { id: string }): Chat {
  const { id: uid, ...chatData } = data;
  return new Chat({ uid, ...chatData });
}

/**
 * Create new chat with optional message.
 *
 * @param {string} message - Optional message to override chat model value.
 * @returns {Promise<ChatInterface>} Current chat.
 */
function createChat(message?: string): Promise<Chat> {
  return apiAgent
    .put('/chat/new', null, { params: { message } })
    .then((response) => apiDataToChat(response.data));
}

/**
 * Update chat with a new message.
 *
 * @param {ChatInterface} chat - Current chat.
 * @param {string} message - New user message.
 * @returns {Promise<ChatInterface>} Updated chat.
 */
function updateChat(chat: Chat, message: string): Promise<Chat> {
  return apiAgent
    .put(`/chat/id/${chat.uid}`, null, { params: { message } })
    .then((response) => apiDataToChat(response.data));
}

/**
 * Request an answer from LLM.
 *
 * @param {ChatInterface} chat - Current chat, or undefined to create a new one.
 * @param {string} message - Chat message to append.
 * @returns {Promise<ChatInterface>} Updated chat.
 */
export function requestAgentAnswer(
  chat: Chat | undefined,
  message?: string,
): Promise<Chat> {
  if (!chat) return createChat(message);
  else if (message !== undefined) return updateChat(chat, message);
  else return Promise.resolve(chat);
}
