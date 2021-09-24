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

const findAll = async () => {
    const books = await executeQuery(`SELECT * FROM books`);
    return books as Book[];
}

const findById = async (id : number) => {
    const book = await executeQueryFindFirst(`SELECT * FROM books where id = (?)`, [id]);
    //parei em 36:38

}

export const bookModel = {
    insertBook,
    findAll
}