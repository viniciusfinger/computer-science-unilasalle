import { Router } from "express";
import { bookController } from "../controllers/books";

const bookRouter = Router();
bookRouter.post('/', bookController.insertBook);
bookRouter.get('/', bookController.findAll);
bookRouter.get('/:id', bookController.findById);
bookRouter.put('/',bookController.update);
bookRouter.delete('/:id', bookController.remove);


export { bookRouter };