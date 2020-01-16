import{ Request, Response} from 'express';
import pool from '../database'

class GamesController {


    public async list (req: Request, res: Response): Promise<void>{
        await pool.query('SELECT * FROM kekomatik', function (error, results, fields) {
            if (error) throw error;
            res.json(results);
          });
          //res.json({message: 'Games showed'});
    }

    

    public async getOne (req: Request, res: Response): Promise<void>{
        const { id } = req.params; 
        await pool.query('SELECT * FROM kekomatik WHERE id = ?', [id], function (error, results, fields) {
            if (error) throw error;
            res.json(results);
          });
    } 

    public async create (req: Request, res: Response ): Promise<void> {
        await pool.query("INSERT INTO kekomatik set ?", [req.body]);
        res.json({message: 'Game Saved'});
    }

    public async delete (req: Request, res: Response ): Promise<void>{
        const { id } = req.params; 
        await pool.query("DELETE FROM kekomatik WHERE id = ?", [id]);
        res.json({text: 'deleting a game ' + req.params.id});
    }

    public async update (req: Request, res: Response ): Promise<void>{
        const { id } = req.params;
        await pool.query("UPDATE kekomatik set ? WHERE id = ?", [req.body, id]);
        res.json({text: 'updating a game ' + req.params.id});
    }

}
const gamesController = new GamesController();
export default gamesController;