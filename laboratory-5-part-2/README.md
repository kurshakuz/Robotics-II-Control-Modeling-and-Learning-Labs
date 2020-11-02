# Laboratory 5. Part 2

Robot manipulator motion modelling.

### 1st approach 
Joint positions PID using gains only.
![](./images/Screenshot_1.png)

### 2nd approach
Joint positions PID + gravity compensation. Without inertia and mass, without velocity compensation
![](./images/without_inertia/Screenshot_2.png)

Joint positions PID + gravity compensation + joint velocity PID. Without inertia and mass, with velocity compensation.
![](./images/without_inertia/Screenshot_3.png)

### 3rd approach
Joint positions PID + inverse dynamic model. With inertia and mass, without velocity compensation.
![](./images/with_inertia/Screenshot_4.png)

Joint positions PID + inverse dynamic model + joint velocity PID. With inertia and mass, with velocity compensation.
![](./images/with_inertia/Screenshot_5.png)