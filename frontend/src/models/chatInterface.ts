export enum ChatRole {
  user = 'user',
  agent = 'agent',
  system = 'system',
  function = 'function',
}

export interface ChatMessageProps {
  role: ChatRole;
  content: string;
  date?: Date;
}

export interface ChatProps {
  uid: string;
  messages: ChatMessageProps[];
  summary?: string | undefined;
  creationDate?: Date;
}
