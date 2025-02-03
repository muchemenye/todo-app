export interface Todo {
    id: number;
    title: string;
    completed: boolean;
}

export interface ApiResponse<T> {
    data: T;
    message: string;
    success: boolean;
}