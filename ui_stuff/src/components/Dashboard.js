import React, {Component} from 'react';
import Grid from "@material-ui/core/Grid";
import DashboardAppBar from "./DashboardAppBar";
import Hosts from "./Hosts";
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline'

class Dashboard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            show: "hosts",
        };
    }

    render() {
        const {show} = this.state
        const darkTheme = createMuiTheme({palette: {type: 'dark',},});

        let info;
        if (show === "hosts") {
            info = <Hosts dashboard={this}/>;
        }

        return (
            <Grid container direction="column">
                <ThemeProvider theme={darkTheme}>
                    <CssBaseline/>
                    <DashboardAppBar dashboard={this}/>
                    <Grid container direction="row" style={{paddingTop: "10px"}}>
                        <Grid item style={{width: '100%'}}>
                            {info}
                        </Grid>
                    </Grid>
                </ThemeProvider>
            </Grid>
        );
    }
}

export default Dashboard;
