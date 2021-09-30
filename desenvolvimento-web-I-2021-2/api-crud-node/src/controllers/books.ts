import {Request, Response } from 'express';
import { Book, bookModel } from '../models/book';
import { badRequest, internalServerError, objectNotFound } from '../services/utils';

const insertBook = (req : Request, res: Response) => {
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
    return bookModel.insertBook(book)
    .then(id => {
        res.json({
            id
        })
    })
    .catch(err => internalServerError(res, err));
}   

const update = (req : Request, res: Response) => {
    {
        const book = req.body;
        if(!book){
            return badRequest(res, "Invalid book.");
        }
        if(!book.id){
            return badRequest(res, "Book must have an id.");
        }
        if(!book.name){
            return badRequest(res, "Book must have a name.");
        }
        if(!book.description){
            return badRequest(res, "Book must have a description.");
        }
    }

    const book = req.body as Book;
    return bookModel.update(book)
    .then(book => {
        res.json({
            book
        })
    })
    .catch(err => internalServerError(res, err));
}  

const findAll = (req : Request, res: Response) => {
    return bookModel.findAll()
    .then(books => {
        res.json({
            books
        })
    })
    .catch(err => internalServerError(res, err));
}
const findById = (req : Request, res: Response) => {
    const id = parseInt(req.params.id);
    {        
        if(id<=0){
            return badRequest(res, "id menor que zero.")
        }
    }

    return bookModel.findById(id)
    .then(book => {
        if(book){
            return res.json({book});
        } else {
            return objectNotFound(res);
        }
    })
    .catch(err => internalServerError(res, err));
}

const remove = (req : Request, res: Response) => {
    const id = parseInt(req.params.id);
    {        
        if(id<=0){
            return badRequest(res, "id menor que zero.")
        }
    }

    return bookModel.remove(id)
    .then(() => res.sendStatus(200)
    ).catch(err => internalServerError(res, err));
}

export const bookController = {
    insertBook,
    findAll,
    findById,
    remove,
    update
}