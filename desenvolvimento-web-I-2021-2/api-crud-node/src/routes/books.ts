import { Router } from "express";
import { productController } from "../controllers/books";

const bookRouter = Router();
bookRouter.post('/', productController.insertProduct);
bookRouter.get('/', productController.findAll);

export { bookRouter };