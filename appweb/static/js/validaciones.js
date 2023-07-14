function ValidarRut(rut){

    if(rut.length >= 9 && rut.length <= 10){

        return true;
    }
    return false;

}

function ValidarNombre(nombre){

    if(nombre.length>=3 && nombre.length<=20){

        return true;
    }
    return false;

}

function ValidarApellido(Apellido){

    if(Apellido.length>=3 && Apellido.length<=20){

        return true;
    }
    return false;

}

function ValidarCorreo(correo){

    if(correo.length>=3 && correo.length<=20){

        return true;
    }
    return false;

}

function ValidarPassword(password){

    if(password.length>=3 && password.length<=20){

        return true;
    }
    return false;

}

function ValidarConfirm_password(confirm_password, password){

    if(confirm_password == password){

        return true;
    }
    return false;

}

function ValidarTipo_cuenta(Tipo_cuenta){

    if(Tipo_cuenta != ""){

        return true;

    }
    return false;

}



function ValidarRechazo(Rechazo){

    if(Rechazo.length>=10 && Rechazo.length<=200){

        return true;
    }
    return false;

}

function ValidarDiagnóstico(diagnóstico){

    if(diagnóstico.length>=10 && diagnóstico.length<=200){

        return true;
    }
    return false;

}

function Validarlistado(listado_materiales){

    if(listado_materiales.length>=10 && listado_materiales.length<=200){

        return true;
    }
    return false;

}

function ValidarNombre_mecanico(nombre_mecanico){

    if(nombre_mecanico.length>=3 && nombre_mecanico.length<=20){

        return true;
    }
    return false;

}

function ValidarApellido_mecanico(Apellido_mecanico){

    if(Apellido_mecanico.length>=3 && Apellido_mecanico.length<=20){

        return true;
    }
    return false;

}

function ValidarFecha(fecha){

    if(fecha != ""){

        return true;

    }
    return false;
}

function ValidarImagen(imagen){

    if(imagen != ""){

        return true;

    }
    return false;
}


function Validarmotivo(motivo){

    if(motivo.length>=10 && motivo.length<=200){

        return true;
    }
    return false;

}