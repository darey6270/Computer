import React from 'react'
import PageHeader from '../../components/PageHeader'
import PeopleOutlineIcon from '@material-ui/icons/PeopleOutline';
import EmployeeForm from './EmployeeForm'
import { makeStyles, Paper } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    pageContent: {
        margin: theme.spacing(5),
        padding:theme.spacing(3),
    }
}))


export default function Employees() {
    const classes = useStyles();
    return (
        <>
            <PageHeader
                title="New Employee" subTitle="Form design with validation"
                icon={<PeopleOutlineIcon fontSize="large" />}
            />
            <Paper className={classes.pageContent}>
            <EmployeeForm />
            </Paper>
        </ >
    )
}
