/* eslint-disable no-console */
import React, { Component } from "react";
import SearchBar from "../../components/SearchBar";
import queryString from "query-string";

class TitlesResults extends Component {
  state = {
    searchString: ""
  }
  
  componentDidMount(){
    // eslint-disable-next-line react/prop-types
    const values = queryString.parse(this.props.location.search)

    if (values != undefined ) {
      this.setState({ searchString: Object.keys(values)[0] })
    }
  }

  render() {
    const { searchString } = this.state

    return (
        <div id="container p-4 my-5">

          <div
            className="opening-blurb border rounded p-4 text-center text-white bg-primary"
          >
            <span role="img" aria-label="emoji" style={{fontSize: 50}}>
              📚
            </span>
            <h2 className="m-0">Search Results: { searchString }</h2>
          </div>

          <div className="flex-container pt-2"> 
            <SearchBar
              value={ searchString }
            />
          </div>
        </div>
    );
  }
}

export default TitlesResults;