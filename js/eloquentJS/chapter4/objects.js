let object1 = {value: 10};
let object2 = object1;
let object3 = {value: 10};

console.log(object1 == object2);
console.log(object1 == object3);

object1.value = 15;
console.log(object2.value);
console.log(object3.value);


/* 
  The object1 and object2 bindings grasp the same object, which is why changing object1 also changes the value of object2. 
  They are said to have the same identity. The binding object3 points to a different object, which initially contains the 
  same properties as object1 but lives a separate life. Bindings can also be changeable or constant, but this is separate 
  from theway their values behave. Even though number values don’t change, you can use a let binding to keep track of a 
  changing number by changing the value the binding points at. Similarly, though a const binding to an object can itself 
  not be changed and will continue to point at the same object, the contents of that object might change.
*/

