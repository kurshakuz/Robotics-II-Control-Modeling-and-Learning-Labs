# Laboratory 5. Part 2

Robot manipulator motion modelling.

### 1st approach 
Joint positions PID using gains only.
![](./images/without_inertia/Screenshot from 2020-11-02 19-08-51.png)

### 2nd approach
Joint positions PID + gravity compensation. Without inertia and mass, without velocity compensation
![](./images/without_inertia/Screenshot from 2020-11-02 19-16-04.png)

Joint positions PID + gravity compensation + joint velocity PID. Without inertia and mass, with velocity compensation.
![](./images/without_inertia/Screenshot from 2020-11-02 19-17-01.png)

### 3rd approach
Joint positions PID + inverse dynamic model. With inertia and mass, without velocity compensation.
![](./images/without_inertia/Screenshot from 2020-11-02 19-10-40.png)

Joint positions PID + inverse dynamic model + joint velocity PID. With inertia and mass, with velocity compensation.
![](./images/without_inertia/Screenshot from 2020-11-02 19-13-22.png)


