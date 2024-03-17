import sqlite3 from 'sqlite3';

const DATABASE_FILE = './data.db';

export const openConnection = () => {
    return new sqlite3.Database(DATABASE_FILE);
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