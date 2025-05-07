import { ChatRole, type ChatProps, type ChatMessageProps } from './chatInterface';
export { ChatRole };

export class ChatMessage implements ChatMessageProps {
  role: ChatRole;
  content: string;
  date?: Date;

  constructor(props: ChatMessageProps) {
    this.role = props.role;
    this.content = props.content;
    this.date = props.date ? new Date(props.date) : new Date();
  }
}

export class Chat implements ChatProps {
  uid: string;
  messages: ChatMessageProps[];
  summary?: string | undefined;
  creationDate?: Date;

  get lastMessage(): ChatMessage | undefined {
    return [...this.messages].sort(
      (a, b) => (b.date ?? new Date(0)).getTime() - (a.date ?? new Date(0)).getTime(),
    )[this.messages.length - 1];
  }

  get lastUpdate() {
    return this.lastMessage?.date ?? this.creationDate ?? new Date(0);
  }

  get length() {
    return this.messages.length;
  }

  constructor(props: ChatProps) {
    this.uid = props.uid;
    this.messages = props.messages.map((message) => new ChatMessage(message));
    this.summary = props.summary;
    this.creationDate = props.creationDate ? new Date(props.creationDate) : new Date();
  }

  /**
   * Append a new message to the messages array.
   *
   * @param {ChatMessage} message - The message to be appended.
   */
  append(message: ChatMessage) {
    this.messages.push(message);
  }
}
