import sqlite3 from 'sqlite3';

const DATABASE_FILE = process.env.DATABASE_FILE;
if (!DATABASE_FILE){
    throw new Error("CAMINHO PARA O BANCO DE DADOS SQLITE NÃO INFORMADO.");
}

export const openConnection = () => {
    let db = new sqlite3.Database(DATABASE_FILE);
    return db;
}

export const executeQuery = (query : string, params?: any[]) => {
    let db = openConnection();
    
    return new Promise<any[]>((resolve, reject) => {
        db.all(query, params, (err, rows) => {
            if (err){
                reject(err);                
            } else {
                resolve(rows);
            }
        })
    }).finally(() => {
        db.close();
    })
}
export const executeQueryFindFirst = async (query : string, params?: any[]) => {
    const result = await executeQuery(query, params);
    return result[0];
}      