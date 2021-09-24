import {Request, Response } from 'express';
import { Book, bookModel } from '../models/book';
import { badRequest, internalServerError } from '../services/utils';

const insertProduct = (req : Request, res: Response) => {
    {
        const book = req.body;
        if(!book){
            return badRequest(res, "Invalid book.");
        }
        if(!book.name){
            return badRequest(res, "Book must have a name.");
        }
        if(!book.description){
            return badRequest(res, "Book must have a description.");
        }
    }

    const book = req.body as Book;
    bookModel.insertBook(book)
    .then(id => {
        res.json({
            id
        })
    })
    .catch(err => internalServerError(res, err));
}   

const findAll = (req : Request, res: Response) => {
    bookModel.findAll()
    .then(books => {
        res.json({
            books
        })
    })
    .catch(err => internalServerError(res, err));
}

export const productController = {
    insertProduct,
    findAll
}