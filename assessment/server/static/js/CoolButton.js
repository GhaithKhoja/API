class CoolButton extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            Helping: false
        }
    }

    render(){

        if(this.state.Helping){
            return (
                <>
                <h2>Commands:</h2>
                <h3>Add (Inserts a task to the TODO list)</h3>
                <p>Example: Command: [add] Entry: [Buy Food]</p>
                <h3>Delete (Deletes a task from the TODO list)</h3>
                <p>Example: Command: [delete] Entry: [Shower]</p>
                <h3>Check (Marks a task as completed in the TODO list)</h3>
                <p>Example: Command: [check] Entry: [Visit Family]</p>
                <h3>Uncheck (Marks a task as not completed in the TODO list)</h3>
                <p>Example: Command: [uncheck] Entry: [Feed Bird]</p>
                </>
            )
        }

        return(
            <button onClick={()=> this.setState({Helping: true})}>
                {this.props.customText}
            </button>
        )
    }


}