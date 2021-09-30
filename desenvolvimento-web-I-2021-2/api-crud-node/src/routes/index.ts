import { Application, Router } from "express";
import { bookRouter } from "./books";

export const useRoutes = (app: Application) => {
    const apiRouter = Router();
    apiRouter.use('/books', bookRouter);
    app.use('/api/v1', apiRouter);
}