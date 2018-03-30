import { topLayer } from '/imports/collections/toplayer.js';
Meteor.methods({
  'get.neighborhoodColors': function(){
    try{
			return topLayer.find({}).fetch();
    }catch(e){
      throw new Meteor.Error("Error getting neighborhood colors (wee woo wee woo): " + e);
    }
		return null;
  }
});
