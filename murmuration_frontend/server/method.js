// This method is currently depricated as of 4/15/2018
import { TopLayer } from '/lib/collections';
Meteor.methods({
 'get.neighborhoodColors': function(){
   try{
			return TopLayer.find({}).fetch();
   }catch(e){
     throw new Meteor.Error("Error getting neighborhood colors (wee woo wee woo): " + e);
   }
		return null;
 }
});
