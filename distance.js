class Point{
    constructor(lat, long){
        this.lat = lat
        this.long = long
    }
    radians(n){
        return Math.PI/180*n
    }
    minus(last){
        let rayon = 6371
        let x = this.radians(this.lat - last.lat)
        let y = this.radians(this.long - last.long)
        let a = (
            Math.sin(x/2) * Math.sin(x/2) +
            Math.cos(this.radians(last.lat)) *
            Math.cos(this.radians(this.lat)) * 
            Math.sin(y/2) * Math.sin(y/2)
        )
        let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
        let d = rayon * c
        return d*1000;
    }
}
console.log(new Point(-3.3751795,29.394586).minus(new Point(-3.3751795,29.394588)))
