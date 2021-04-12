import React from 'react'
import { Spinner } from 'react-bootstrap'

function Loader() {
    return (
        <spinner 
            animation='border'
            role='status'
            style ={{
                 height:'100px',
                 width: '100px',
                 margin:'auto',
                 display: 'block',

            }}>
            <span className='sr-only'>Cargando...</span>
        </spinner>
    )
}

export default Loader
