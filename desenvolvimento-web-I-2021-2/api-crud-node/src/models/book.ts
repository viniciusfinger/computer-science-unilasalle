import { executeQuery, executeQueryFindFirst } from "../services/db"

export type Book = {
    id : number;
    name : string;
    description : string;
    ISBNcode : string;
}

const insertBook = async (book : Book ) => {
    await executeQuery(`INSERT INTO books (name, description, isbncode) VALUES (?,?,?)`, [book.name, book.description, book.ISBNcode]);
    let insertedId = await executeQuery(`SELECT seq FROM sqlite_sequence where name = 'books'`);
    return insertedId[0].Id as number || undefined;
}

const update = async (book : Book ) => {
    await executeQuery(`UPDATE books SET name = ?, description = ?, isbncode = ? where id = ?`, [book.name, book.description, book.ISBNcode, book.id]);
    return findById(book.id);
}

const findAll = async () => {
    const books = await executeQuery(`SELECT * FROM books`);
    return books as Book[];
}

const findById = async (id : number) => {
    const book = await executeQueryFindFirst(`SELECT * FROM books where id = (?)`, [id]);
    return book as Book | undefined;
}

const remove = async (id : number) => {
    const book = await executeQuery(`DELETE FROM books where id = (?)`, [id]);
}

export const bookModel = {
    insertBook,
    findAll,
    findById,
    remove,
    update
}