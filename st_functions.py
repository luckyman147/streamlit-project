import streamlit as st 
def load_css():
    
    with open("stt.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    
    if icon == 'github':
        button_code = f'''
        <p>
        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 0a8 8 0 0 0-2.52 15.589c.4.074.546-.174.546-.387 0-.19-.007-.693-.01-1.36-2.223.483-2.695-1.07-2.695-1.07-.364-.924-.888-1.17-.888-1.17-.724-.495.055-.486.055-.486.8.056 1.222.82 1.222.82.712 1.22 1.866.867 2.32.663.072-.516.28-.867.508-1.067-1.777-.2-3.644-.888-3.644-3.953 0-.873.312-1.587.823-2.147-.083-.2-.36-1.015.078-2.117 0 0 .67-.215 2.2.82.638-.178 1.318-.266 2-.27.68.004 1.362.092 2 .27 1.523-1.035 2.192-.82 2.192-.82.44 1.102.163 1.917.08 2.117.512.56.82 1.274.82 2.147 0 3.073-1.87 3.75-3.652 3.947.288.248.54.735.54 1.48 0 1.07-.01 1.93-.01 2.19 0 .214.145.466.55.386A8.001 8.001 0 0 0 8 0"/>
            </svg>
            {label}
        </a>
    </p>'''
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>''' 
    elif icon == 'facebook':
        button_code = f'''
        <p>
        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M14 0H2C.895 0 0 .895 0 2v12c0 1.105.895 2 2 2h6.5v-6.176H6.5V7.31c0-1.806 1.386-3.51 3.584-3.51h2.918v2.824H10.5c-.31 0-.56.25-.56.56v1.863h3.12L13 14h-2.94V16h2.94c1.105 0 2-.895 2-2V2c0-1.105-.895-2-2-2z"/>
            </svg>
            {label}
        </a>
    </p>'''
    

   
    else:
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)


