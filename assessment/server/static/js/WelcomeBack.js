class WelcomeBack extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            name: 'Rob',
        }
    }

    render(){
        return(
            <>
                <h2>Hello {this.state.name || 'Friend'}! Welcome to your TODO List.</h2>
                <p>To read instructions on how to use the list click the help button</p> 
                <CoolButton customText={'Help'} />
            </>
        )
    }


}