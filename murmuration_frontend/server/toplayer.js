var database = new MongoInternals.RemoteCollectionDriver('mongodb://localhost:3001/layer_bank');
export const topLayer = database.open('toplayer');
