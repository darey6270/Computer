import { FormControl, FormControlLabel, FormLabel, Grid, makeStyles, Radio, RadioGroup, TextField } from '@material-ui/core';
import React, { useState } from 'react'
import { useForm, Form } from '../../components/useForm';
import { Controls } from '../../components/controls/Controls';



const initialFValues = {
    id: 0,
    fullName: '',
    email: '',
    mobile: '',
    city:'',
    gender:'male',
    departmentId: '',
    hireDate: new Date(),
    isPermanent:false,
 };

const genderItems = [
    { id: 'male', title: 'Male' },
    { id: 'female', title: 'Female' },
    { id: 'other', title: 'Other' }
];


export default function EmployeeForm() {
    const {values ,setValues, handleInputChange}=useForm(initialFValues)

    return (
<Form>
            <Grid container>
                <Grid item xs={6}>
                <Controls.Input
                        name="FullName"
                        label="Full Name"
                        value={values.fullName} onChange={handleInputChange} />
                <Controls.Input
                        label="Email"
                        name="email"
                        value={values.email}  onChange={handleInputChange} />
                    </Grid>
                    <Grid item xs={6}>
                        <Controls.RadioGroup 
                        name="gender" items={genderItems}
                        value={values.gender} onChange={handleInputChange}
                        />
                </Grid>
    </Grid>

</Form>
    )
}