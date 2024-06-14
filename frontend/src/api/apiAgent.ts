import { apiAgent } from 'src/boot/axios';
import { Chat } from 'src/models/chat';
import type { ChatMessageProps, ChatProps } from 'src/models/chatInterface';

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
function apiDataToChat(
  data: Omit<ChatProps, 'uid' | 'creationDate' | 'messages'> & {
    id: string;
    creation_datetime: Date;
    messages: (Omit<ChatMessageProps, 'date'> & { datetime: Date })[];
  },
): Chat {
  const {
    id: uid,
    creation_datetime: creationDate,
    messages: apiMessages,
    ...chatData
  } = data;
  const messages = apiMessages.map((apiMessage) => {
    const { datetime: date, ...message } = apiMessage;
    return { ...message, date: date };
  });
  return new Chat({ uid, creationDate, messages, ...chatData });
}

/**
 * Retrieve all chats from chat history.
 *
 * @returns {Promise<Chat[]>} Chats.
 */
export function getChats(): Promise<Chat[]> {
  return apiAgent
    .get('/chat/history')
    .then((response) => response.data.map(apiDataToChat));
}

/**
 * Create new chat with optional message.
 *
 * @param {string} message - Optional message to override chat model value.
 * @param {boolean} reply - Whether to request a reply from agent.
 * @returns {Promise<ChatInterface>} Current chat.
 */
function createChat(message?: string, reply?: boolean): Promise<Chat> {
  return apiAgent
    .post('/chat/new', null, { params: { message, reply } })
    .then((response) => apiDataToChat(response.data));
}

/**
 * Update chat with a new message.
 *
 * @param {ChatInterface} chat - Current chat.
 * @param {string} message - New user message.
 * @param {boolean} reply - Whether to request a reply from agent.
 * @returns {Promise<ChatInterface>} Updated chat.
 */
function updateChat(
  chat: Chat,
  message: string,
  reply?: boolean,
): Promise<Chat> {
  return apiAgent
    .post(`/chat/id/${chat.uid}`, null, { params: { message, reply } })
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
  if (!chat) return createChat(message, true);
  else if (message !== undefined) return updateChat(chat, message, true);
  else return Promise.resolve(chat);
}
