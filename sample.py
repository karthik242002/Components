input_box = [
    {"html": """<div class="form-group">
    <span>{btn1}</span>
    <input class="form-field" type="text" placeholder={plh1}
</div> """,
     "css": """:root {

    --input-color: #99A3BA;
    --input-border: #CDD9ED;
    --input-background: #fff;
    --input-placeholder: #CBD1DC;

    --input-border-focus: #275EFE;

    --group-color: var(--input-color);
    --group-border: var(--input-border);
    --group-background: #EEF4FF;

    --group-color-focus: #fff;
    --group-border-focus: var(--input-border-focus);
    --group-background-focus: #678EFE;

}

.form-field {
    display: block;
    width: 100%;
    padding: 8px 16px;
    line-height: 25px;
    font-size: 14px;
    font-weight: 500;
    font-family: inherit;
    border-radius: 6px;
    -webkit-appearance: none;
    color: var(--input-color);
    border: 1px solid var(--input-border);
    background: var(--input-background);
    transition: border .3s ease;
    &::placeholder {
        color: var(--input-placeholder);
    }
    &:focus {
        outline: none;
        border-color: var(--input-border-focus);
    }
}

.form-group {
    position: relative;
    display: flex;
    width: 100%;
    & > span,
    .form-field {
        white-space: nowrap;
        display: block;
        &:not(:first-child):not(:last-child) {
            border-radius: 0;
        }
        &:first-child {
            border-radius: 6px 0 0 6px;
        }
        &:last-child {
            border-radius: 0 6px 6px 0;
        }
        &:not(:first-child) {
            margin-left: -1px;
        }
    }
    .form-field {
        position: relative;
        z-index: 1;
        flex: 1 1 auto;
        width: 1%;
        margin-top: 0;
        margin-bottom: 0;
    }
    & > span {
        text-align: center;
        padding: 8px 12px;
        font-size: 14px;
        line-height: 25px;
        color: var(--group-color);
        background: var(--group-background);
        border: 1px solid var(--group-border);
        transition: background .3s ease, border .3s ease, color .3s ease;
    }
    &:focus-within {
        & > span {
            color: var(--group-color-focus);
            background: var(--group-background-focus);
            border-color: var(--group-border-focus);
        }
    }
}

html {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
}

* {
    box-sizing: inherit;
    &:before,
    &:after {
        box-sizing: inherit;
    }
}

// Center
body {
    min-height: 100vh;
    font-family: 'Mukta Malar', Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background: #F5F9FF;  
    .form-group {
        max-width: 360px;
        &:not(:last-child) {
            margin-bottom: 32px;
        }
    }
} """,
     "js": """ """,},
    
    {"html": """<div class="form-group">
    <input class="form-field" type="email" placeholder={plh1}>
    <span>{btn1}</span>
</div> """,
     "css": """:root {

    --input-color: #99A3BA;
    --input-border: #CDD9ED;
    --input-background: #fff;
    --input-placeholder: #CBD1DC;

    --input-border-focus: #275EFE;

    --group-color: var(--input-color);
    --group-border: var(--input-border);
    --group-background: #EEF4FF;

    --group-color-focus: #fff;
    --group-border-focus: var(--input-border-focus);
    --group-background-focus: #678EFE;

}

.form-field {
    display: block;
    width: 100%;
    padding: 8px 16px;
    line-height: 25px;
    font-size: 14px;
    font-weight: 500;
    font-family: inherit;
    border-radius: 6px;
    -webkit-appearance: none;
    color: var(--input-color);
    border: 1px solid var(--input-border);
    background: var(--input-background);
    transition: border .3s ease;
    &::placeholder {
        color: var(--input-placeholder);
    }
    &:focus {
        outline: none;
        border-color: var(--input-border-focus);
    }
}

.form-group {
    position: relative;
    display: flex;
    width: 100%;
    & > span,
    .form-field {
        white-space: nowrap;
        display: block;
        &:not(:first-child):not(:last-child) {
            border-radius: 0;
        }
        &:first-child {
            border-radius: 6px 0 0 6px;
        }
        &:last-child {
            border-radius: 0 6px 6px 0;
        }
        &:not(:first-child) {
            margin-left: -1px;
        }
    }
    .form-field {
        position: relative;
        z-index: 1;
        flex: 1 1 auto;
        width: 1%;
        margin-top: 0;
        margin-bottom: 0;
    }
    & > span {
        text-align: center;
        padding: 8px 12px;
        font-size: 14px;
        line-height: 25px;
        color: var(--group-color);
        background: var(--group-background);
        border: 1px solid var(--group-border);
        transition: background .3s ease, border .3s ease, color .3s ease;
    }
    &:focus-within {
        & > span {
            color: var(--group-color-focus);
            background: var(--group-background-focus);
            border-color: var(--group-border-focus);
        }
    }
}

html {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
}

* {
    box-sizing: inherit;
    &:before,
    &:after {
        box-sizing: inherit;
    }
}

// Center
body {
    min-height: 100vh;
    font-family: 'Mukta Malar', Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background: #F5F9FF;  
    .form-group {
        max-width: 360px;
        &:not(:last-child) {
            margin-bottom: 32px;
        }
    }
} """,
     "js": """ """,},
    
    {"html": """<div class="form__group field">
  <input type="input" class="form__field" placeholder={plh1} name="name" id='name' required />
  <label for="name" class="form__label">Name</label>
</div> """,
     "css": """$primary: #11998e;
$secondary: #38ef7d;
$white: #fff;
$gray: #9b9b9b;
.form__group {
  position: relative;
  padding: 15px 0 0;
  margin-top: 10px;
  width: 50%;
}

.form__field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 2px solid $gray;
  outline: 0;
  font-size: 1.3rem;
  color: $white;
  padding: 7px 0;
  background: transparent;
  transition: border-color 0.2s;

  &::placeholder {
    color: transparent;
  }

  &:placeholder-shown ~ .form__label {
    font-size: 1.3rem;
    cursor: text;
    top: 20px;
  }
}

.form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: $gray;
}

.form__field:focus {
  ~ .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 1rem;
    color: $primary;
    font-weight:700;    
  }
  padding-bottom: 6px;  
  font-weight: 700;
  border-width: 3px;
  border-image: linear-gradient(to right, $primary,$secondary);
  border-image-slice: 1;
}
/* reset input */
.form__field{
  &:required,&:invalid { box-shadow:none; }
}
/* demo */
body {
  font-family: 'Poppins', sans-serif; 
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  font-size: 1.5rem;
  background-color:#222222;
} """,
     "js": """ """,},
    
    {"html": """<div class="container">
	<div>
		<h4 class="title">Underlined Inputs</h4>
		<form>
			<div class="omrs-input-group">
				<label class="omrs-input-underlined">
				  <input required>
				  <span class="omrs-input-label">Normal</span>
					<span class="omrs-input-helper">Helper Text</span>
				<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0V0z"/><circle cx="15.5" cy="9.5" r="1.5"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm-5-6c.78 2.34 2.72 4 5 4s4.22-1.66 5-4H7z"/></svg>
				</label>
			</div>
 """,
     "css": """/** BEGIN: Non Openmrs CSS **/
@import url("https://fonts.googleapis.com/css?family=Roboto&display=swap");
* {
	font-family: "Roboto";
}
div.container {
	display: flex;
	align-items: flex-start;
	justify-content: space-around;
	margin-top: 30px;
	border: 1px solid whitesmoke;
	padding: 21px;
	border-radius: 4px;
}
h4.title {
	text-align: center;
	margin-bottom: 45px;
}
:root {
	--omrs-color-ink-lowest-contrast: rgba(47, 60, 85, 0.18);
	--omrs-color-ink-low-contrast: rgba(60, 60, 67, 0.3);
	--omrs-color-ink-medium-contrast: rgba(19, 19, 21, 0.6);
	--omrs-color-interaction: #1e4bd1;
	--omrs-color-interaction-minus-two: rgba(73, 133, 224, 0.12);
	--omrs-color-danger: #b50706;
	--omrs-color-bg-low-contrast: #eff1f2;
	--omrs-color-ink-high-contrast: #121212;
	--omrs-color-bg-high-contrast: #ffffff;
	
}
/** END: Non Openmrs CSS **/
div.omrs-input-group {
  margin-bottom: 1.5rem;
  position: relative;
  width: 20.4375rem;
}

/* Input*/
.omrs-input-underlined > input,
.omrs-input-filled > input {
	border: none;
	border-bottom: 0.125rem solid var(--omrs-color-ink-medium-contrast);
	width: 100%;
	height: 2rem;
	font-size: 1.0625rem;
	padding-left: 0.875rem;
	line-height: 147.6%;
	padding-top: 0.825rem;
	padding-bottom: 0.5rem;
}

.omrs-input-underlined > input:focus,
.omrs-input-filled > input:focus {
	outline: none;
}

.omrs-input-underlined > .omrs-input-label,
.omrs-input-filled > .omrs-input-label {
	position: absolute;
	top: 0.9375rem;
	left: 0.875rem;
	line-height: 147.6%;
	color: var(--omrs-color-ink-medium-contrast);
	transition: top .2s;
}

.omrs-input-underlined > svg,
.omrs-input-filled > svg {
	position: absolute;
	top: 0.9375rem;
	right: 0.875rem;
	fill: var(--omrs-color-ink-medium-contrast);
}

.omrs-input-underlined > .omrs-input-helper,
.omrs-input-filled > .omrs-input-helper {
	font-size: 0.9375rem;
	color: var(--omrs-color-ink-medium-contrast);
	letter-spacing: 0.0275rem;
	margin: 0.125rem 0.875rem;
}

.omrs-input-underlined > input:hover,
.omrs-input-filled > input:hover {
	background: var(--omrs-color-interaction-minus-two);
	border-color: var(--omrs-color-ink-high-contrast);
}

.omrs-input-underlined > input:focus + .omrs-input-label,
.omrs-input-underlined > input:valid + .omrs-input-label,
.omrs-input-filled > input:focus + .omrs-input-label,
.omrs-input-filled > input:valid + .omrs-input-label {
	top: 0;
	font-size: 0.9375rem;
	margin-bottom: 32px;;
}

.omrs-input-underlined:not(.omrs-input-danger) > input:focus + .omrs-input-label,
.omrs-input-filled:not(.omrs-input-danger) > input:focus + .omrs-input-label {
	color: var(--omrs-color-interaction);
}

.omrs-input-underlined:not(.omrs-input-danger) > input:focus,
.omrs-input-filled:not(.omrs-input-danger) > input:focus {
	border-color: var(--omrs-color-interaction);
}

.omrs-input-underlined:not(.omrs-input-danger) > input:focus ~ svg,
.omrs-input-filled:not(.omrs-input-danger) > input:focus ~ svg {
	fill: var(--omrs-color-ink-high-contrast);
}

/** DISABLED **/

.omrs-input-underlined > input:disabled {
	background: var(--omrs-color-bg-low-contrast);
	cursor: not-allowed;
}

.omrs-input-underlined > input:disabled + .omrs-input-label,
.omrs-input-underlined > input:disabled ~ .omrs-input-helper{
	color: var(--omrs-color-ink-low-contrast);
}

.omrs-input-underlined > input:disabled ~ svg {
	fill: var(--omrs-color-ink-low-contrast);
}


/** DANGER **/

.omrs-input-underlined.omrs-input-danger > .omrs-input-label, .omrs-input-underlined.omrs-input-danger > .omrs-input-helper,
.omrs-input-filled.omrs-input-danger > .omrs-input-label, .omrs-input-filled.omrs-input-danger > .omrs-input-helper{
	color: var(--omrs-color-danger);
}

.omrs-input-danger > svg {
	fill: var(--omrs-color-danger);
}

.omrs-input-danger > input {
	border-color: var(--omrs-color-danger);
}

.omrs-input-underlined > input {
	background: var(--omrs-color-bg-high-contrast);
}
.omrs-input-filled > input {
	background: var(--omrs-color-bg-low-contrast);
} """,
     "js": """ """,},
    
    {"html": """<div class="box">
	<form>
		<span class="text-center">login</span>
	<div class="input-container">
		<input type="text" required=""/>
		<label>Full Name</label>		
	</div>
	<div class="input-container">		
		<input type="mail" required=""/>
		<label>Email</label>
	</div>
		<button type="button" class="btn">submit</button>
</form>	
</div> """,
     "css": """@import url('https://fonts.googleapis.com/css?family=Noto+Sans:400,400i,700,700i&subset=greek-ext');

body{
	background-image: url("https://images.pexels.com/photos/891252/pexels-photo-891252.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260");
	background-position: center;
    background-origin: content-box;
    background-repeat: no-repeat;
    background-size: cover;
	min-height:100vh;
	font-family: 'Noto Sans', sans-serif;
}
.text-center{
	color:#fff;	
	text-transform:uppercase;
    font-size: 23px;
    margin: -50px 0 80px 0;
    display: block;
    text-align: center;
}
.box{
	position:absolute;
	left:50%;
	top:50%;
	transform: translate(-50%,-50%);
    background-color: rgba(0, 0, 0, 0.89);
	border-radius:3px;
	padding:70px 100px;
}
.input-container{
	position:relative;
	margin-bottom:25px;
}
.input-container label{
	position:absolute;
	top:0px;
	left:0px;
	font-size:16px;
	color:#fff;	
    pointer-event:none;
	transition: all 0.5s ease-in-out;
}
.input-container input{ 
  border:0;
  border-bottom:1px solid #555;  
  background:transparent;
  width:100%;
  padding:8px 0 5px 0;
  font-size:16px;
  color:#fff;
}
.input-container input:focus{ 
 border:none;	
 outline:none;
 border-bottom:1px solid #e74c3c;	
}
.btn{
	color:#fff;
	background-color:#e74c3c;
	outline: none;
    border: 0;
    color: #fff;
	padding:10px 20px;
	text-transform:uppercase;
	margin-top:50px;
	border-radius:2px;
	cursor:pointer;
	position:relative;
}
/*.btn:after{
	content:"";
	position:absolute;
	background:rgba(0,0,0,0.50);
	top:0;
	right:0;
	width:100%;
	height:100%;
}*/
.input-container input:focus ~ label,
.input-container input:valid ~ label{
	top:-12px;
	font-size:12px;
	
}
 """,
     "js": """ """,},
    
    {"html": """<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<div class="form__group">
  <input type="text" class="form__input" id="name" placeholder="Full name" required="" />
  <label for="name" class="form__label">Full Name</label>
</div>
 """,
     "css": """*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: inherit;
  font-size: 62,5%;
}

body {
  height: 100vh;
	width: 100%;
  background: #0f2027; /* fallback for old browsers */
  background: linear-gradient(to right,#2c5364, #203a43, #0f2027);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #fff;
}

.form__label {
  font-family: 'Roboto', sans-serif;
  font-size: 1.2rem;
  margin-left: 2rem;
  margin-top: 0.7rem;
  display: block;
  transition: all 0.3s;
  transform: translateY(0rem);
}

.form__input {
  font-family: 'Roboto', sans-serif;
  color: #333;
  font-size: 1.2rem;
	margin: 0 auto;
  padding: 1.5rem 2rem;
  border-radius: 0.2rem;
  background-color: rgb(255, 255, 255);
  border: none;
  width: 90%;
  display: block;
  border-bottom: 0.3rem solid transparent;
  transition: all 0.3s;
}

.form__input:placeholder-shown + .form__label {
  opacity: 0;
  visibility: hidden;
  -webkit-transform: translateY(-4rem);
  transform: translateY(-4rem);
}
 """,
     "js": """ """,},
    
    {"html": """<input class="c-checkbox" type="checkbox" id="checkbox">
<div class="c-formContainer">
  <form class="c-form" action="">
    <input class="c-form__input" placeholder="E-mail" type="email" pattern="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$" required>
    <label class="c-form__buttonLabel" for="checkbox">
      <button class="c-form__button" type="button">Send</button>
    </label>
    <label class="c-form__toggle" for="checkbox" data-title="Notify me"></label>
  </form>
</div> """,
     "css": """$black: #000000;
$cornflower-lilac: #ffaea9;
$salmon: #ff7b73;
$white: #ffffff;
$your-pink: #ffcccc;

body {
    font-size: 10px; // change value to scale
    font-family: Roboto, sans-serif;
    background-color: $salmon;
    
    margin: 0;
    display: grid;
    height: 100vh;
    place-items: center;
}

.c-checkbox {
    display: none;

    &:checked + .c-formContainer {
        .c-form {
            width: 37.5em;
        }

        .c-form__toggle {
            visibility: hidden;
            opacity: 0;
            transform: scale(0.7);
        }

        .c-form__input,
        .c-form__buttonLabel {
            transition: 0.2s 0.1s;
            visibility: visible;
            opacity: 1;
            transform: scale(1);
        }
    }

    &:not(:checked),
    &:checked {
        + .c-formContainer .c-form__input:required:valid ~ .c-form__toggle::before {
            content: 'Thank You! \1F60A';
        }
    }

    &:not(:checked) + .c-formContainer {
        .c-form__input:required:valid ~ .c-form__toggle {
            pointer-events: none;
            cursor: default;
        }
    }
}

.c-formContainer,
.c-form,
.c-form__toggle {
    width: 20em;
    height: 6.25em;
}

.c-formContainer {
    position: relative;
    font-weight: 700;
}

.c-form,
.c-form__toggle {
    position: absolute;
    border-radius: 6.25em;
    background-color: $white;
    transition: 0.2s;
}

.c-form {
    left: 50%;
    transform: translateX(-50%);
    padding: 0.625em;
    box-sizing: border-box;
    box-shadow: 0 0.125em 0.3125em rgba($black, 0.3);

    // position form inputs
    display: flex;
    justify-content: center;
}

.c-form__toggle {
    color: $salmon;
    top: 0;
    cursor: pointer;
    z-index: 1;

    // position message
    display: flex;
    align-items: center;
    justify-content: center;

    &::before {
        font-size: 1.75em;
        content: attr(data-title);
    }
}

.c-form__input,
.c-form__button {
    font: inherit;
    border: 0;
    outline: 0;
    border-radius: 5em;
    box-sizing: border-box;
}

.c-form__input,
.c-form__buttonLabel {
    font-size: 1.75em;
    opacity: 0;
    visibility: hidden;
    transform: scale(0.7);
    transition: 0s;
}

.c-form__input {
    color: $your-pink;
    height: 100%;
    width: 100%;
    padding: 0 0.714em;

    &::placeholder {
        color: currentColor;
    }

    &:required:valid {
        color: $salmon;

        + .c-form__buttonLabel {
            color: $white;

            &::before {
                pointer-events: initial;
            }
        }
    }
}

.c-form__buttonLabel {
    color: $cornflower-lilac;
    height: 100%;
    width: auto;
    
    // accepts click events
    &::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        pointer-events: none;
        cursor: pointer;
    }
}

.c-form__button {
    color: inherit;
    padding: 0;
    height: 100%;
    width: 5em;
    background-color: $salmon;
} """,
     "js": """// Simple registration form: https://codepen.io/bertdida/full/XxZjNy/ """,},
    
    {"html": """<label for="inp" class="inp">
  <input type="password" id="inp" placeholder="Password" pattern=".{6,}" required>
  <svg width="280px" height="18px" viewBox="0 0 280 18" class="border">
    <path d="M0,12 L223.166144,12 C217.241379,12 217.899687,12 225.141066,12 C236.003135,12 241.9279,12 249.827586,12 C257.727273,12 264.639498,12 274.514107,12 C281.097179,12 281.755486,12 276.489028,12"></path>
  </svg>
  <svg width="14px" height="12px" viewBox="0 0 14 12" class="check">
    <path d="M1 7 5.5 11 L13 1"></path>
  </svg>
</label>
</form> """,
     "css": """$primary = #0077FF

html, body
  height: 100%

body
  display: grid
  font-family: Avenir
  -webkit-text-size-adjust: 100%
  -webkit-font-smoothing: antialiased
  overflow: hidden
  
*
  box-sizing: border-box
  
.inp
  position: relative
  margin: auto
  width: 100%
  max-width: 280px
  height: 53px
  .border
    position: absolute
    left: 0
    bottom: 0
    height: 18px
    fill: none
    path
      stroke: #C8CCD4
      stroke-width: 2
      d
        transition: all .2s ease
  .check
    position: absolute
    top: 20px
    right: 20px
    fill: none
    transform: translate(0,9px) scale(0)
    transition: all .3s cubic-bezier(.5, .9, .25, 1.3)
    transition-delay: .15s
    path
      stroke: $primary
      stroke-width: 2 

  input
    -webkit-appearance: none
    width: 100%
    border: 0
    font-family: inherit
    padding: 0
    height: 48px
    font-size: 16px
    font-weight: 500
    background: none
    border-radius: 0
    color: #223254
    transition: all .15s ease
    &:focus
      outline: none
      + .border path
        stroke: $primary
    &:valid
      + .border 
        path
          animation: elasticInput .8s ease forwards
        + .check
          transform: translate(0,0) scale(1)
        
::placeholder
  color: #9098A9
      
@keyframes elasticInput
  33%
    d: path("M0,12 L226,12 C220,12 220.666667,12 228,12 C239,12 245,1 253,1 C261,1 268,12 278,12 C284.666667,12 285.333333,12 280,12")
  66%
    d: path("M0,12 L226,12 C220,12 220.666667,12 228,12 C239,12 245,17 253,17 C261,17 268,12 278,12 C284.666667,12 285.333333,12 280,12") """,
     "js": """ """,},
    
    {"html": """<div class="mahi_holder">
    <div class="container">
      <div class="row bg_1">
        <h2><i>Border effects</i></h2>
        <div class="col-3">
            <input class="effect-1" type="text" placeholder="Placeholder Text">
              <span class="focus-border"></span>
          </div>
        <div class="col-3">
            <input class="effect-2" type="text" placeholder="Placeholder Text">
              <span class="focus-border"></span>
          </div>
        <div class="col-3">
            <input class="effect-3" type="text" placeholder="Placeholder Text">
              <span class="focus-border"></span>
          </div>        
        <div class="col-3">
            <input class="effect-4" type="text" placeholder="Placeholder Text">
              <span class="focus-border"></span>
          </div>
        <div class="col-3">
            <input class="effect-5" type="text" placeholder="Placeholder Text">
              <span class="focus-border"></span>
          </div>
        <div class="col-3">
            <input class="effect-6" type="text" placeholder="Placeholder Text">
              <span class="focus-border"></span>
          </div>        
        <div class="col-3">
            <input class="effect-7" type="text" placeholder="Placeholder Text">
              <span class="focus-border">
                <i></i>
              </span>
          </div>
        <div class="col-3">
            <input class="effect-8" type="text" placeholder="Placeholder Text">
              <span class="focus-border">
                <i></i>
              </span>
          </div>
        <div class="col-3">
            <input class="effect-9" type="text" placeholder="Placeholder Text">
              <span class="focus-border">
                <i></i>
              </span>
          </div>
      </div> 
      <div class="row bg_2">
        <h2><i>Background Effects</i></h2>
        <div class="col-3">
        	<input class="effect-10" type="text" placeholder="Placeholder Text">
            <span class="focus-bg"></span>
        </div>
        <div class="col-3">
        	<input class="effect-11" type="text" placeholder="Placeholder Text">
            <span class="focus-bg"></span>
        </div>
        <div class="col-3">
        	<input class="effect-12" type="text" placeholder="Placeholder Text">
            <span class="focus-bg"></span>
        </div>
        <div class="col-3">
        	<input class="effect-13" type="text" placeholder="Placeholder Text">
            <span class="focus-bg"></span>
        </div>
        <div class="col-3">
        	<input class="effect-14" type="text" placeholder="Placeholder Text">
            <span class="focus-bg"></span>
        </div>
        <div class="col-3">
        	<input class="effect-15" type="text" placeholder="Placeholder Text">
            <span class="focus-bg"></span>
        </div>
      </div>
      <div class="row bg_3">
        <h2><i>Input with Label Effects</i></h2>
        <div class="col-3 input-effect">
        	<input class="effect-16" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-border"></span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-17" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-border"></span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-18" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-border"></span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-19" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-border">
            	<i></i>
            </span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-20" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-border">
            	<i></i>
            </span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-21" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-border">
            	<i></i>
            </span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-22" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-bg"></span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-23" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-bg"></span>
        </div>
        <div class="col-3 input-effect">
        	<input class="effect-24" type="text" placeholder="">
            <label>First Name</label>
            <span class="focus-bg"></span>
        </div>
      </div>
    </div>
</div>
 """,
     "css": """@import url('https://fonts.googleapis.com/css?family=Damion|Muli:400,600');
body{
  font-family: 'Muli', sans-serif;
  background: url("https://www.toptal.com/designers/subtlepatterns/patterns/geometry2.png");
}
h2 {
    font-family: 'Damion', cursive;
    font-weight: 400;
    color: #4caf50;
    font-size: 35px;
    text-align: center;
    position: relative;
}
h2:before {
    position: absolute;
    content: '';
    width: 100%;
    left: 0;
    top: 22px;
    background: #4caf50;
    height: 1px;
}
h2 i {
    font-style: normal;
    background: #fff;
    position: relative;
    padding: 10px;
}
:focus{outline: none;}

/* necessary to give position: relative to parent. */
input[type="text"]{font: 15px/24px 'Muli', sans-serif; color: #333; width: 100%; box-sizing: border-box; letter-spacing: 1px;}

:focus{outline: none;}

.col-3{float: left; width: 27.33%; margin: 40px 3%; position: relative;} /* necessary to give position: relative to parent. */
input[type="text"]{font: 15px/24px "Lato", Arial, sans-serif; color: #333; width: 100%; box-sizing: border-box; letter-spacing: 1px;}

.effect-1, 
.effect-2, 
.effect-3{border: 0; padding: 7px 0; border-bottom: 1px solid #ccc;}

.effect-1 ~ .focus-border{position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background-color: #4caf50; transition: 0.4s;}
.effect-1:focus ~ .focus-border{width: 100%; transition: 0.4s;}

.effect-2 ~ .focus-border{position: absolute; bottom: 0; left: 50%; width: 0; height: 2px; background-color: #4caf50; transition: 0.4s;}
.effect-2:focus ~ .focus-border{width: 100%; transition: 0.4s; left: 0;}

.effect-3 ~ .focus-border{position: absolute; bottom: 0; left: 0; width: 100%; height: 2px; z-index: 99;}
.effect-3 ~ .focus-border:before, 
.effect-3 ~ .focus-border:after{content: ""; position: absolute; bottom: 0; left: 0; width: 0; height: 100%; background-color: #4caf50; transition: 0.4s;}
.effect-3 ~ .focus-border:after{left: auto; right: 0;}
.effect-3:focus ~ .focus-border:before, 
.effect-3:focus ~ .focus-border:after{width: 50%; transition: 0.4s;}

.effect-4,
.effect-5,
.effect-6{border: 0; padding: 5px 0 7px; border: 1px solid transparent; border-bottom-color: #ccc; transition: 0.4s;}

.effect-4:focus,
.effect-5:focus,
.effect-6:focus{padding: 5px 14px 7px; transition: 0.4s;}

.effect-4 ~ .focus-border{position: absolute; height: 0; bottom: 0; left: 0; width: 100%; transition: 0.4s; z-index: -1;}
.effect-4:focus ~ .focus-border{transition: 0.4s; height: 36px; border: 2px solid #4caf50; z-index: 1;}

.effect-5 ~ .focus-border{position: absolute; height: 36px; bottom: 0; left: 0; width: 0; transition: 0.4s;}
.effect-5:focus ~ .focus-border{width: 100%; transition: 0.4s; border: 2px solid #4caf50;}

.effect-6 ~ .focus-border{position: absolute; height: 36px; bottom: 0; right: 0; width: 0; transition: 0.4s;}
.effect-6:focus ~ .focus-border{width: 100%; transition: 0.4s; border: 2px solid #4caf50;}

.effect-7,
.effect-8,
.effect-9{border: 1px solid #ccc; padding: 7px 14px 9px; transition: 0.4s;}

.effect-7 ~ .focus-border:before,
.effect-7 ~ .focus-border:after{content: ""; position: absolute; top: 0; left: 50%; width: 0; height: 2px; background-color: #4caf50; transition: 0.4s;}
.effect-7 ~ .focus-border:after{top: auto; bottom: 0;}
.effect-7 ~ .focus-border i:before,
.effect-7 ~ .focus-border i:after{content: ""; position: absolute; top: 50%; left: 0; width: 2px; height: 0; background-color: #4caf50; transition: 0.6s;}
.effect-7 ~ .focus-border i:after{left: auto; right: 0;}
.effect-7:focus ~ .focus-border:before,
.effect-7:focus ~ .focus-border:after{left: 0; width: 100%; transition: 0.4s;}
.effect-7:focus ~ .focus-border i:before,
.effect-7:focus ~ .focus-border i:after{top: 0; height: 100%; transition: 0.6s;}

.effect-8 ~ .focus-border:before,
.effect-8 ~ .focus-border:after{content: ""; position: absolute; top: 0; left: 0; width: 0; height: 2px; background-color: #4caf50; transition: 0.3s;}
.effect-8 ~ .focus-border:after{top: auto; bottom: 0; left: auto; right: 0;}
.effect-8 ~ .focus-border i:before,
.effect-8 ~ .focus-border i:after{content: ""; position: absolute; top: 0; left: 0; width: 2px; height: 0; background-color: #4caf50; transition: 0.4s;}
.effect-8 ~ .focus-border i:after{left: auto; right: 0; top: auto; bottom: 0;}
.effect-8:focus ~ .focus-border:before,
.effect-8:focus ~ .focus-border:after{width: 100%; transition: 0.3s;}
.effect-8:focus ~ .focus-border i:before,
.effect-8:focus ~ .focus-border i:after{height: 100%; transition: 0.4s;}

.effect-9 ~ .focus-border:before,
.effect-9 ~ .focus-border:after{content: ""; position: absolute; top: 0; right: 0; width: 0; height: 2px; background-color: #4caf50; transition: 0.2s; transition-delay: 0.2s;}
.effect-9 ~ .focus-border:after{top: auto; bottom: 0; right: auto; left: 0; transition-delay: 0.6s;}
.effect-9 ~ .focus-border i:before,
.effect-9 ~ .focus-border i:after{content: ""; position: absolute; top: 0; left: 0; width: 2px; height: 0; background-color: #4caf50; transition: 0.2s;}
.effect-9 ~ .focus-border i:after{left: auto; right: 0; top: auto; bottom: 0; transition-delay: 0.4s;}
.effect-9:focus ~ .focus-border:before,
.effect-9:focus ~ .focus-border:after{width: 100%; transition: 0.2s; transition-delay: 0.6s;}
.effect-9:focus ~ .focus-border:after{transition-delay: 0.2s;}
.effect-9:focus ~ .focus-border i:before,
.effect-9:focus ~ .focus-border i:after{height: 100%; transition: 0.2s;}
.effect-9:focus ~ .focus-border i:after{transition-delay: 0.4s;}

.effect-10, 
.effect-11, 
.effect-12,
.effect-13,
.effect-14,
.effect-15{border: 0; padding: 7px 15px; border: 1px solid #ccc; position: relative; background: transparent;}

.effect-10 ~ .focus-bg{position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: #ededed; opacity: 0; transition: 0.5s; z-index: -1;}
.effect-10:focus ~ .focus-bg{transition: 0.5s; opacity: 1;}

.effect-11 ~ .focus-bg{position: absolute; left: 0; top: 0; width: 0; height: 100%; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-11:focus ~ .focus-bg{transition: 0.3s; width: 100%;}

.effect-12 ~ .focus-bg{position: absolute; left: 50%; top: 0; width: 0; height: 100%; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-12:focus ~ .focus-bg{transition: 0.3s; width: 100%; left: 0;}

.effect-13 ~ .focus-bg:before,
.effect-13 ~ .focus-bg:after{content: ""; position: absolute; left: 0; top: 0; width: 0; height: 100%; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-13:focus ~ .focus-bg:before{transition: 0.3s; width: 50%;}
.effect-13 ~ .focus-bg:after{left: auto; right: 0;}
.effect-13:focus ~ .focus-bg:after{transition: 0.3s; width: 50%;}

.effect-14 ~ .focus-bg:before,
.effect-14 ~ .focus-bg:after{content: ""; position: absolute; left: 0; top: 0; width: 0; height: 0; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-14:focus ~ .focus-bg:before{transition: 0.3s; width: 50%; height: 100%;}
.effect-14 ~ .focus-bg:after{left: auto; right: 0; top: auto; bottom: 0;}
.effect-14:focus ~ .focus-bg:after{transition: 0.3s; width: 50%; height: 100%;}

.effect-15 ~ .focus-bg:before,
.effect-15 ~ .focus-bg:after{content: ""; position: absolute; left: 50%; top: 50%; width: 0; height: 0; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-15:focus ~ .focus-bg:before{transition: 0.3s; width: 50%; left: 0; top: 0; height: 100%;}
.effect-15 ~ .focus-bg:after{left: auto; right: 50%; top: auto; bottom: 50%;}
.effect-15:focus ~ .focus-bg:after{transition: 0.3s; width: 50%; height: 100%; bottom: 0; right: 0;}


.effect-16, 
.effect-17, 
.effect-18{border: 0; padding: 4px 0; border-bottom: 1px solid #ccc; background-color: transparent;}

.effect-16 ~ .focus-border{position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background-color: #4caf50; transition: 0.4s;}
.effect-16:focus ~ .focus-border,
.has-content.effect-16 ~ .focus-border{width: 100%; transition: 0.4s;}
.effect-16 ~ label{position: absolute; left: 0; width: 100%; top: 9px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-16:focus ~ label, .has-content.effect-16 ~ label{top: -16px; font-size: 12px; color: #4caf50; transition: 0.3s;}

.effect-17 ~ .focus-border{position: absolute; bottom: 0; left: 50%; width: 0; height: 2px; background-color: #4caf50; transition: 0.4s;}
.effect-17:focus ~ .focus-border,
.has-content.effect-17 ~ .focus-border{width: 100%; transition: 0.4s; left: 0;}
.effect-17 ~ label{position: absolute; left: 0; width: 100%; top: 9px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-17:focus ~ label, .has-content.effect-17 ~ label{top: -16px; font-size: 12px; color: #4caf50; transition: 0.3s;}

.effect-18 ~ .focus-border{position: absolute; bottom: 0; left: 0; width: 100%; height: 2px; z-index: 99;}
.effect-18 ~ .focus-border:before, 
.effect-18 ~ .focus-border:after{content: ""; position: absolute; bottom: 0; left: 0; width: 0; height: 100%; background-color: #4caf50; transition: 0.4s;}
.effect-18 ~ .focus-border:after{left: auto; right: 0;}
.effect-18:focus ~ .focus-border:before, 
.effect-18:focus ~ .focus-border:after,
.has-content.effect-18 ~ .focus-border:before,
.has-content.effect-18 ~ .focus-border:after{width: 50%; transition: 0.4s;}
.effect-18 ~ label{position: absolute; left: 0; width: 100%; top: 9px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-18:focus ~ label, .has-content.effect-18 ~ label{top: -16px; font-size: 12px; color: #4caf50; transition: 0.3s;}

.effect-19,
.effect-20,
.effect-21{border: 1px solid #ccc; padding: 7px 14px; transition: 0.4s; background: transparent;}

.effect-19 ~ .focus-border:before,
.effect-19 ~ .focus-border:after{content: ""; position: absolute; top: -1px; left: 50%; width: 0; height: 2px; background-color: #4caf50; transition: 0.4s;}
.effect-19 ~ .focus-border:after{top: auto; bottom: 0;}
.effect-19 ~ .focus-border i:before,
.effect-19 ~ .focus-border i:after{content: ""; position: absolute; top: 50%; left: 0; width: 2px; height: 0; background-color: #4caf50; transition: 0.6s;}
.effect-19 ~ .focus-border i:after{left: auto; right: 0;}
.effect-19:focus ~ .focus-border:before,
.effect-19:focus ~ .focus-border:after,
.has-content.effect-19 ~ .focus-border:before,
.has-content.effect-19 ~ .focus-border:after{left: 0; width: 100%; transition: 0.4s;}
.effect-19:focus ~ .focus-border i:before,
.effect-19:focus ~ .focus-border i:after,
.has-content.effect-19 ~ .focus-border i:before,
.has-content.effect-19 ~ .focus-border i:after{top: -1px; height: 100%; transition: 0.6s;}
.effect-19 ~ label{position: absolute; left: 14px; width: 100%; top: 10px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-19:focus ~ label, .has-content.effect-19 ~ label{top: -18px; left: 0; font-size: 12px; color: #4caf50; transition: 0.3s;}

.effect-20 ~ .focus-border:before,
.effect-20 ~ .focus-border:after{content: ""; position: absolute; top: 0; left: 0; width: 0; height: 2px; background-color: #4caf50; transition: 0.3s;}
.effect-20 ~ .focus-border:after{top: auto; bottom: 0; left: auto; right: 0;}
.effect-20 ~ .focus-border i:before,
.effect-20 ~ .focus-border i:after{content: ""; position: absolute; top: 0; left: 0; width: 2px; height: 0; background-color: #4caf50; transition: 0.4s;}
.effect-20 ~ .focus-border i:after{left: auto; right: 0; top: auto; bottom: 0;}
.effect-20:focus ~ .focus-border:before,
.effect-20:focus ~ .focus-border:after,
.has-content.effect-20 ~ .focus-border:before,
.has-content.effect-20 ~ .focus-border:after{width: 100%; transition: 0.3s;}
.effect-20:focus ~ .focus-border i:before,
.effect-20:focus ~ .focus-border i:after,
.has-content.effect-20 ~ .focus-border i:before,
.has-content.effect-20 ~ .focus-border i:after{height: 100%; transition: 0.4s;}
.effect-20 ~ label{position: absolute; left: 14px; width: 100%; top: 10px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-20:focus ~ label, .has-content.effect-20 ~ label{top: -18px; left: 0; font-size: 12px; color: #4caf50; transition: 0.3s;}

.effect-21 ~ .focus-border:before,
.effect-21 ~ .focus-border:after{content: ""; position: absolute; top: 0; right: 0; width: 0; height: 2px; background-color: #4caf50; transition: 0.2s; transition-delay: 0.2s;}
.effect-21 ~ .focus-border:after{top: auto; bottom: 0; right: auto; left: 0; transition-delay: 0.6s;}
.effect-21 ~ .focus-border i:before,
.effect-21 ~ .focus-border i:after{content: ""; position: absolute; top: 0; left: 0; width: 2px; height: 0; background-color: #4caf50; transition: 0.2s;}
.effect-21 ~ .focus-border i:after{left: auto; right: 0; top: auto; bottom: 0; transition-delay: 0.4s;}
.effect-21:focus ~ .focus-border:before,
.effect-21:focus ~ .focus-border:after,
.has-content.effect-21 ~ .focus-border:before,
.has-content.effect-21 ~ .focus-border:after{width: 100%; transition: 0.2s; transition-delay: 0.6s;}
.effect-21:focus ~ .focus-border:after,
.has-content.effect-21 ~ .focus-border:after{transition-delay: 0.2s;}
.effect-21:focus ~ .focus-border i:before,
.effect-21:focus ~ .focus-border i:after,
.has-content.effect-21 ~ .focus-border i:before,
.has-content.effect-21 ~ .focus-border i:after{height: 100%; transition: 0.2s;}
.effect-21:focus ~ .focus-border i:after,
.has-conten.effect-21 ~ .focus-border i:after{transition-delay: 0.4s;}
.effect-21 ~ label{position: absolute; left: 14px; width: 100%; top: 10px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-21:focus ~ label, .has-content.effect-21 ~ label{top: -18px; left: 0; font-size: 12px; color: #4caf50; transition: 0.3s;}

.effect-22, 
.effect-23, 
.effect-24{border: 0; padding: 7px 15px; border: 1px solid #ccc; position: relative; background: transparent;}

.effect-22 ~ .focus-bg{position: absolute; left: 0; top: 0; width: 0; height: 100%; background-color: transparent; transition: 0.4s; z-index: -1;}
.effect-22:focus ~ .focus-bg, 
.has-content.effect-22 ~ .focus-bg{transition: 0.4s; width: 100%; background-color: #ededed;}
.effect-22 ~ label{position: absolute; left: 14px; width: 100%; top: 10px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-22:focus ~ label, .has-content.effect-22 ~ label{top: -18px; left: 0; font-size: 12px; color: #333; transition: 0.3s;}

.effect-23 ~ .focus-bg:before,
.effect-23 ~ .focus-bg:after{content: ""; position: absolute; left: 0; top: 0; width: 0; height: 0; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-23:focus ~ .focus-bg:before,
.has-content.effect-23 ~ .focus-bg:before{transition: 0.3s; width: 50%; height: 100%;}
.effect-23 ~ .focus-bg:after{left: auto; right: 0; top: auto; bottom: 0;}
.effect-23:focus ~ .focus-bg:after,
.has-content.effect-23 ~ .focus-bg:after{transition: 0.3s; width: 50%; height: 100%;}
.effect-23 ~ label{position: absolute; left: 14px; width: 100%; top: 10px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-23:focus ~ label, .has-content.effect-23 ~ label{top: -18px; left: 0; font-size: 12px; color: #333; transition: 0.3s;}

.effect-24 ~ .focus-bg:before,
.effect-24 ~ .focus-bg:after{content: ""; position: absolute; left: 50%; top: 50%; width: 0; height: 0; background-color: #ededed; transition: 0.3s; z-index: -1;}
.effect-24:focus ~ .focus-bg:before,
.has-content.effect-24 ~ .focus-bg:before{transition: 0.3s; width: 50%; left: 0; top: 0; height: 100%;}
.effect-24 ~ .focus-bg:after{left: auto; right: 50%; top: auto; bottom: 50%;}
.effect-24:focus ~ .focus-bg:after,
.has-content.effect-24 ~ .focus-bg:after{transition: 0.3s; width: 50%; height: 100%; bottom: 0; right: 0;}
.effect-24 ~ label{position: absolute; left: 14px; width: 100%; top: 10px; color: #aaa; transition: 0.3s; z-index: -1; letter-spacing: 0.5px;}
.effect-24:focus ~ label, .has-content.effect-24 ~ label{top: -18px; left: 0; font-size: 12px; color: #333; transition: 0.3s;}
 """,
     "js": """ """,},
    
    {"html": """
<p>
	<span class="input">
		<input type="text" placeholder="Gradient border focus fun">
		<span></span>	
	</span>
</p>
 """,
     "css": """.input {
	
	// needs to be relative so the :focus span is positioned correctly
	position:relative;
	
	// bigger font size for demo purposes
	font-size: 1.5em;
	
	// the border gradient
	background: linear-gradient(21deg, #10abff, #1beabd);
	
	// the width of the input border
	padding: 3px;
	
	// we want inline fields by default
	display: inline-block;
	
	// we want rounded corners no matter the size of the field
	border-radius: 9999em;
	
	// style of the actual input field
	*:not(span) {
		position: relative;
		display: inherit;
		border-radius: inherit;
		margin: 0;
		border: none;
		outline: none;
		padding: 0 .325em;
		z-index: 1; // needs to be above the :focus span
		
		// summon fancy shadow styles when focussed
		&:focus + span {
			opacity: 1;
			transform: scale(1);
		}
	}
	
	// we don't animate box-shadow directly as that can't be done on the GPU, only animate opacity and transform for high performance animations.
	span {
		
		transform: scale(.993, .94); // scale it down just a little bit
		transition: transform .5s, opacity .25s;
		opacity: 0; // is hidden by default
		
		position:absolute;
		z-index: 0; // needs to be below the field (would block input otherwise)
		margin:4px; // a bit bigger than .input padding, this prevents background color pixels shining through
		left:0;
		top:0;
		right:0;
		bottom:0;
		border-radius: inherit;
		pointer-events: none; // this allows the user to click through this element, as the shadow is rather wide it might overlap with other fields and we don't want to block those.
		
		// fancy shadow styles
		box-shadow: inset 0 0 0 3px #fff,
			0 0 0 4px #fff,
			3px -3px 30px #1beabd, 
			-3px 3px 30px #10abff;
	}
	
}

html {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
	line-height:1.5;
	font-size:1em;
}

body {
	text-align: center;
	display:flex;
	align-items: center;
	justify-content: center;
}

html, body {
	height:100%;
}

input {
	font-family: inherit;
	line-height:inherit;
	color:#2e3750;
	min-width:12em;
}

::placeholder {
	color:#cbd0d5;
}

html::after {
	content:'';
	background: linear-gradient(21deg, #10abff, #1beabd);
	height:3px;
	width:100%;
	position:absolute;
	left:0;
	top:0;
} """,
     "js": """ """,},
    
    {"html": """<div class="Wrapper">
  <h1 class="Title">CSS Only Floated Labels!</h1>
  <div class="Input">
    <input type="text" id="input" class="Input-text" placeholder="Your first name, e.g. Nicholas">
    <label for="input" class="Input-label">First name</label>
  </div>
</div> """,
     "css": """ @import url('https://fonts.googleapis.com/css?family=Dosis');

:root {
  /* generic */
  --gutterSm: 0.4rem;
  --gutterMd: 0.8rem;
  --gutterLg: 1.6rem;
  --gutterXl: 2.4rem;
  --gutterXx: 7.2rem;
  --colorPrimary400: #7e57c2;
  --colorPrimary600: #5e35b1;
  --colorPrimary800: #4527a0;
  --fontFamily: "Dosis", sans-serif;
  --fontSizeSm: 1.2rem;
  --fontSizeMd: 1.6rem;
  --fontSizeLg: 2.1rem;
  --fontSizeXl: 2.8rem;
  --fontSizeXx: 3.6rem;
  --lineHeightSm: 1.1;
  --lineHeightMd: 1.8;
  --transitionDuration: 300ms;
  --transitionTF: cubic-bezier(0.645, 0.045, 0.355, 1);
  
  /* floated labels */
  --inputPaddingV: var(--gutterMd);
  --inputPaddingH: var(--gutterLg);
  --inputFontSize: var(--fontSizeLg);
  --inputLineHeight: var(--lineHeightMd);
  --labelScaleFactor: 0.8;
  --labelDefaultPosY: 50%;
  --labelTransformedPosY: calc(
    (var(--labelDefaultPosY)) - 
    (var(--inputPaddingV) * var(--labelScaleFactor)) - 
    (var(--inputFontSize) * var(--inputLineHeight))
  );
  --inputTransitionDuration: var(--transitionDuration);
  --inputTransitionTF: var(--transitionTF);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  font-size: 10px;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  width: 100vw;
  height: 100vh;
  color: #455A64;
  background-color: #7E57C2;
  font-family: var(--fontFamily);
  font-size: var(--fontSizeMd);
  line-height: var(--lineHeightMd);
}

.Wrapper {
  flex: 0 0 80%;
  max-width: 80%;
}

.Title {
  margin: 0 0 var(--gutterXx) 0;
  padding: 0;
  color: #fff;
  font-size: var(--fontSizeXx);
  font-weight: 400;
  line-height: var(--lineHeightSm);
  text-align: center;
  text-shadow: -0.1rem 0.1rem 0.2rem var(--colorPrimary800);
}

.Input {
  position: relative;
}

.Input-text {
  display: block;
  margin: 0;
  padding: var(--inputPaddingV) var(--inputPaddingH);
  color: inherit;
  width: 100%;
  font-family: inherit;
  font-size: var(--inputFontSize);
  font-weight: inherit;
  line-height: var(--inputLineHeight);
  border: none;
  border-radius: 0.4rem;
  transition: box-shadow var(--transitionDuration);
}

.Input-text::placeholder {
  color: #B0BEC5;
}

.Input-text:focus {
  outline: none;
  box-shadow: 0.2rem 0.8rem 1.6rem var(--colorPrimary600);
}

.Input-label {
  display: block;
  position: absolute;
  bottom: 50%;
  left: 1rem;
  color: #fff;
  font-family: inherit;
  font-size: var(--inputFontSize);
  font-weight: inherit;
  line-height: var(--inputLineHeight);
  opacity: 0;
  transform: 
    translate3d(0, var(--labelDefaultPosY), 0)
    scale(1);
  transform-origin: 0 0;
  transition:
    opacity var(--inputTransitionDuration) var(--inputTransitionTF),
    transform var(--inputTransitionDuration) var(--inputTransitionTF),
    visibility 0ms var(--inputTransitionDuration) var(--inputTransitionTF),
    z-index 0ms var(--inputTransitionDuration) var(--inputTransitionTF);
}

.Input-text:placeholder-shown + .Input-label {
  visibility: hidden;
  z-index: -1;
}

.Input-text:not(:placeholder-shown) + .Input-label,
.Input-text:focus:not(:placeholder-shown) + .Input-label {
  visibility: visible;
  z-index: 1;
  opacity: 1;
  transform:
    translate3d(0, var(--labelTransformedPosY), 0)
    scale(var(--labelScaleFactor));
  transition:
    transform var(--inputTransitionDuration),
    visibility 0ms,
    z-index 0ms;
}""",
     "js": """/*

No JS!

Floated labels made using only CSS and the :placeholder-shown pseudo class. Read more about it out here:

https://developer.mozilla.org/en-US/docs/Web/CSS/:placeholder-shown

Browser support for <input type="text">:

Chrome:   47
Firefox:  51
IE:       No support
Edge:     No support
Opera:    34
Safari:   9

*/ """,},
    
    {"html": """<div class="page">
  <div class="field field_v1">
    <label for="first-name" class="ha-screen-reader">First name</label>
    <input id="first-name" class="field__input" placeholder="e.g. Stanislav">
    <span class="field__label-wrap" aria-hidden="true">
      <span class="field__label">First name</span>
    </span>
  </div>
  <div class="field field_v2">
    <label for="last-name" class="ha-screen-reader">Last name</label>
    <input id="last-name"  class="field__input" placeholder="e.g. Melnikov">
    <span class="field__label-wrap" aria-hidden="true">
      <span class="field__label">Last name</span>
    </span>
  </div>    
  <div class="field field_v3">
    <label for="email" class="ha-screen-reader">E-mail</label>
    <input id="email" class="field__input" placeholder="e.g. melnik909@ya.ru">
    <span class="field__label-wrap" aria-hidden="true">
      <span class="field__label">E-mail</span>
    </span>
  </div>
</div>
<div class="linktr">
  <a href="https://cssisntmagic.substack.com" target="_blank" class="linktr__goal r-link">Subscribe on my email newsletter with CSS tips 💪💪💪</a>
</div> """,
     "css": """/*
=====
HELPERS
=====
*/

.ha-screen-reader{
  width: var(--ha-screen-reader-width, 1px);
  height: var(--ha-screen-reader-height, 1px);
  padding: var(--ha-screen-reader-padding, 0);
  border: var(--ha-screen-reader-border, none);

  position: var(--ha-screen-reader-position, absolute);
  clip: var(--ha-screen-reader-clip, rect(1px, 1px, 1px, 1px));
  overflow: var(--ha-screen-reader-overflow, hidden);
}

/*
=====
RESET STYLES
=====
*/

.field__input{ 
  --uiFieldPlaceholderColor: var(--fieldPlaceholderColor, #767676);
  
  background-color: transparent;
  border-radius: 0;
  border: none;

  -webkit-appearance: none;
  -moz-appearance: none;

  font-family: inherit;
  font-size: inherit;
}

.field__input:focus::-webkit-input-placeholder{
  color: var(--uiFieldPlaceholderColor);
}

.field__input:focus::-moz-placeholder{
  color: var(--uiFieldPlaceholderColor);
}

/*
=====
CORE STYLES
=====
*/

.field{
  --uiFieldBorderWidth: var(--fieldBorderWidth, 2px);
  --uiFieldPaddingRight: var(--fieldPaddingRight, 1rem);
  --uiFieldPaddingLeft: var(--fieldPaddingLeft, 1rem);   
  --uiFieldBorderColorActive: var(--fieldBorderColorActive, rgba(22, 22, 22, 1));

  display: var(--fieldDisplay, inline-flex);
  position: relative;
  font-size: var(--fieldFontSize, 1rem);
}

.field__input{
  box-sizing: border-box;
  width: var(--fieldWidth, 100%);
  height: var(--fieldHeight, 3rem);
  padding: var(--fieldPaddingTop, 1.25rem) var(--uiFieldPaddingRight) var(--fieldPaddingBottom, .5rem) var(--uiFieldPaddingLeft);
  border-bottom: var(--uiFieldBorderWidth) solid var(--fieldBorderColor, rgba(0, 0, 0, .25));  
}

.field__input:focus{
  outline: none;
}

.field__input::-webkit-input-placeholder{
  opacity: 0;
  transition: opacity .2s ease-out;
}

.field__input::-moz-placeholder{
  opacity: 0;
  transition: opacity .2s ease-out;
}

.field__input:focus::-webkit-input-placeholder{
  opacity: 1;
  transition-delay: .2s;
}

.field__input:focus::-moz-placeholder{
  opacity: 1;
  transition-delay: .2s;
}

.field__label-wrap{
  box-sizing: border-box;
  pointer-events: none;
  cursor: text;

  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.field__label-wrap::after{
  content: "";
  box-sizing: border-box;
  width: 100%;
  height: 0;
  opacity: 0;

  position: absolute;
  bottom: 0;
  left: 0;
}

.field__input:focus ~ .field__label-wrap::after{
  opacity: 1;
}

.field__label{
  position: absolute;
  left: var(--uiFieldPaddingLeft);
  top: calc(50% - .5em);

  line-height: 1;
  font-size: var(--fieldHintFontSize, inherit);

  transition: top .2s cubic-bezier(0.9, -0.15, 0.1, 1.15), opacity .2s ease-out, font-size .2s ease-out;
}

.field__input:focus ~ .field__label-wrap .field__label,
.field__input:not(:placeholder-shown) ~ .field__label-wrap .field__label{
  --fieldHintFontSize: var(--fieldHintFontSizeFocused, .75rem);

  top: var(--fieldHintTopHover, .25rem);
}

/* 
effect 1
*/

.field_v1 .field__label-wrap::after{
  border-bottom: var(--uiFieldBorderWidth) solid var(--uiFieldBorderColorActive);
  transition: opacity .2s ease-out;
}

/* 
effect 2
*/

.field_v2 .field__label-wrap{
  overflow: hidden;
}

.field_v2 .field__label-wrap::after{
  border-bottom: var(--uiFieldBorderWidth) solid var(--uiFieldBorderColorActive);
  transform: translate3d(-105%, 0, 0);
  transition: transform .285s ease-out .2s, opacity .2s ease-out .2s;
}

.field_v2 .field__input:focus ~ .field__label-wrap::after{
  transform: translate3d(0, 0, 0);
  transition-delay: 0;
}

/*
effect 3
*/

.field_v3 .field__label-wrap::after{
  border: var(--uiFieldBorderWidth) solid var(--uiFieldBorderColorActive);
  transition: height .2s ease-out, opacity .2s ease-out;
}

.field_v3 .field__input:focus ~ .field__label-wrap::after{
  height: 100%;
}

/*
=====
LEVEL 4. SETTINGS
=====
*/

.field{
  --fieldBorderColor: #D1C4E9;
  --fieldBorderColorActive: #673AB7;
}

/*
=====
DEMO
=====
*/

body{
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Open Sans, Ubuntu, Fira Sans, Helvetica Neue, sans-serif;
  margin: 0;

  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.page{
  box-sizing: border-box;
  width: 100%;
  max-width: 480px;
  margin: auto;
  padding: 1rem;

  display: grid;
  grid-gap: 30px;
}

.linktr{
  order: -1;
  padding: 1.75rem;
  text-align: center;
}

.linktr__goal{
  background-color: rgb(209, 246, 255);
  color: rgb(8, 49, 112);
  box-shadow: rgb(8 49 112 / 24%) 0px 2px 8px 0px;
  border-radius: 2rem;
  padding: .5rem 1.25rem;
}

@media (min-width: 1024px){
  
  .linktr{
    position: absolute; 
    right: 1rem; 
    bottom: 1rem;
  }
}

.r-link{
    --uirLinkDisplay: var(--rLinkDisplay, inline-flex);
    --uirLinkTextColor: var(--rLinkTextColor);
    --uirLinkTextDecoration: var(--rLinkTextDecoration, none);

    display: var(--uirLinkDisplay) !important;
    color: var(--uirLinkTextColor) !important;
    text-decoration: var(--uirLinkTextDecoration) !important;
}

 """,
     "js": """ """,},
    
    {"html": """<input maxlength='7' value='0123456'/> """,
     "css": """$char-w: 1ch;
$gap: .5*$char-w;
$n-char: 7;
$in-w: $n-char*($char-w + $gap);

input {
	display: block;
	margin: 2em auto;
	border: none;
	padding: 0;
	width: $in-w;
	background: repeating-linear-gradient(90deg, 
		dimgrey 0, dimgrey $char-w, 
		transparent 0, transparent $char-w + $gap) 
		0 100%/ #{$in-w - $gap} 2px no-repeat;
	font: 5ch droid sans mono, consolas, monospace;
	letter-spacing: $gap;
	
	&:focus {
		outline: none;
		color: dodgerblue;
	}
} """,
     "js": """ """,},
    
    {"html": """<div class="container">
	<div class="container__item">
		<form class="form">
			<input type="email" class="form__field" placeholder="Your E-Mail Address" />
			<button type="button" class="btn btn--primary btn--inside uppercase">Send</button>
		</form>
	</div>
	
	<div class="container__item container__item--bottom">
		<p>Inspired by <a href="//dribbble.com/shots/2989456-Email-input-field" target="_blank">Daniel Luca</a>.</p>
	</div>
</div> """,
     "css": """//** variables
$background: #f5f6fa;
$text: #9c9c9c;
$input-bg-color: #fff;
$input-text-color: #a3a3a3;
$button-bg-color: #7f8ff4;
$button-text-color: #fff;

//** root
:root {
	background: $background;
	color: $text;
	font: 1rem "PT Sans", sans-serif;
}

html,
body,
.container {
	height: 100%;
}

a {
	color: inherit;
	
	&:hover {
		color: $button-bg-color;
	}
}

//** helper
.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}

.uppercase {
	text-transform: uppercase;
}

//** button
.btn {
	display: inline-block;
	background: transparent;
	color: inherit;
	font: inherit;
	border: 0;
	outline: 0;
	padding: 0;
	transition: all 200ms ease-in;
	cursor: pointer;
	
	&--primary {
		background: $button-bg-color;
		color: $button-text-color;
		box-shadow: 0 0 10px 2px rgba(0, 0, 0, .1);
		border-radius: 2px;
		padding: 12px 36px;
		
		&:hover {
			background: darken($button-bg-color, 4%);
		}
		
		&:active {
			background: $button-bg-color;
			box-shadow: inset 0 0 10px 2px rgba(0, 0, 0, .2);
		}
	}
	
	&--inside {
		margin-left: -96px;
	}
}

//** form
.form {	
	&__field {
		width: 360px;
		background: #fff;
		color: $input-text-color;
		font: inherit;
		box-shadow: 0 6px 10px 0 rgba(0, 0, 0 , .1);
		border: 0;
		outline: 0;
		padding: 22px 18px;
	}
} """,
     "js": """ """,},
    
    {"html": """<div id="wrap" class="input">
  <header class="input-header">
    <h1>Input Text/Password Animation</h1>
  </header>
  <section class="input-content">
    <h2>Input Text/Password Animation<span>Only CSS</span></h2>
    <div class="input-content-wrap">
      <dl class="inputbox">
        <dt class="inputbox-title">Input Text</dt>
        <dd class="inputbox-content">
          <input id="input0" type="text" required/>
          <label for="input0">ID</label>
          <span class="underline"></span>
        </dd>
      </dl>
      <dl class="inputbox">
        <dt class="inputbox-title">Input Password</dt>
        <dd class="inputbox-content">
          <input id="input1" type="password" required/>
          <label for="input1">Password</label>
          <span class="underline"></span>
        </dd>
      </dl>
      <div class="btns">
          <button class="btn btn-confirm">Sign In</button>
          <button class="btn btn-cancel">Cancel</button>
      </div>
    </div>
  </section>
</div> """,
     "css": """ // color vars
$primary-color: #1a237e;
$dark-primary-color: #0f1041;
$accent-color: #2962ff;
$sub-yellow: #ffca00;

//common style
html,body{
  height: 100%;
  background: #e0e0e0;
  font-family:sans-serif;
  font-size:14px;
}
#wrap{
  width: 100%;
  max-width:900px;
  margin:0 auto 60px;
  box-shadow: 0 3px 6px rgba(0,0,0,0.25);
}

//layout
.input{
  &::before{
    content:'';
    display:block;
    position: absolute;
    top:0;
    left:0;
    width: 100%;
    height: 300px;
    background: $dark-primary-color;
  }
  &-header{
    position: relative;
    padding-top:80px;
    color: #fff;
    h1{
      padding-bottom:25px;
      font-size:3.25em;
      font-weight:100;
    }
  }
  &-content{
    position: relative;
    padding:44px 55px;
    background: #fff;
    z-index:10;
    
    h2{
      padding-bottom:45px;
      font-size:1.625em;
      font-weight:bold;
      vertical-align: middle;
      span{
        display: inline-block;
        margin-left:10px;
        padding:5px 6px 3px;
        border:1px solid $sub-yellow;
        border-radius:4px;
        font-size:0.85rem;
        vertical-align: middle;
        color: $sub-yellow;
      }
    }
    .inputbox{
      overflow: hidden;
      position: relative;
      padding:15px 0 28px 200px;
      &-title{
        position: absolute;
        top:15px;
        left: 0;
        width: 200px;
        height: 30px;
        color: #666;
        font-weight: bold;
        line-height: 30px;
      }
      &-content{
        position: relative;
        width: 100%;
        input{
          width: 100%;
          height: 30px;
          box-sizing: border-box;
          line-height: 30px;
          font-size:14px;
          border:0;
          background: none;
          border-bottom:1px solid #ccc;
          outline:none;
          border-radius: 0;
          -webkit-appearance: none;
          &:focus,&:valid{
            &~label{
              color: $accent-color;
              transform: translateY(-20px);
              font-size:0.825em;
              cursor:default;
            }
          }
          &:focus{
            &~.underline{
              width: 100%;
            }
          }
        }
        label{
          position: absolute;
          top:0;
          left:0;
          height: 30px;
          line-height: 30px;
          color:#ccc;
          cursor:text;
          transition: all 200ms ease-out;
          z-index:10;
        }
        .underline{
          content:'';
          display: block;
          position: absolute;
          bottom:-1px;
          left:0;
          width: 0;
          height: 2px;
          background: $accent-color;
          transition: all 200ms ease-out;
        }
      }
    }
    
    .btns{
      padding:30px 0 0 200px;
      .btn{
        display:inline-block;
        margin-right:2px;
        padding: 10px 25px;
        background: none;
        border:1px solid #c0c0c0;
        border-radius:2px;
        color: #666;
        font-size:1.125em;
        outline:none;
        transition: all 100ms ease-out;
        &:hover,&:focus{
          transform: translateY(-3px);
        }
        &-confirm{
        border:1px solid $accent-color;
        background: $accent-color;
        color: #fff;}
      }
    }
  }
}""",
     "js": """ """,},
    
    {"html": """.centered
  .group
    input(type="text" id="name" required)
    label(for="name") Name
    .bar """,
     "css": """$main-color: #F44336;
$secondary-color: white;
$main-color: #333;
$secondary-color: #2196f3;
$width: 550px; // Change Me

* {
  box-sizing: border-box;
}

body {background: $main-color;}

.centered {
  width: $width;
  height: $width/5;
  margin: auto;
  position: absolute;
  top: 0; bottom: 0;
  left: 0; right: 0; 
}

.group {
  width: 100%;
  height: $width/5;
  overflow: hidden;
  position: relative;
}

label {
  position: absolute;
  top: $width/15;
  color: rgba(white, .5);
  font: 400 $width/15 Roboto;
  cursor: text;
  transition: .25s ease;
}

input {
  display: block;
  width: 100%;
  padding-top: $width/15;
  border: none;
  border-radius: 0; // For iOS
  // border-bottom: solid $width/150 rgba(white, .5);
  color: white;
  background: $main-color;
  font-size: $width/15;
  transition: .3s ease;
  &:valid {
    // border-bottom-color: rgba(white, .5);
    ~label {
      top: 0;
      font: 700 $width/25 Roboto;
      color: rgba(white, .5);
    }
  }
  &:focus {
    outline: none;
    // border-bottom-color: $secondary-color;
    ~label {
      top: 0;
      font: 700 $width/25 Roboto;
      color: $secondary-color;
    }
    
      
    ~ .bar:before {
    transform: translateX(0);
    }
  }

  // Stop Chrome's hideous pale yellow background on auto-fill
  
  &:-webkit-autofill {
    -webkit-box-shadow: 0 0 0px 1000px $main-color inset;
    -webkit-text-fill-color: white !important;
    // border-bottom-color: rgba(white, .5);
  }
}

.bar {
  // background: $secondary-color;
  background: rgba(white, .5);
  content: '';
  width: $width;
  // height: $width/100;
  height: $width/150;
  // transform: translateX(-100%);
  transition: .3s ease;
  // margin-top: -2px;
  //
  position: relative;
  &:before {
    content: '';
    position: absolute;
    width: 100%;
    height: 150%;
    background: $secondary-color;
    transform: translateX(-100%);
    
  }
}

::selection {background: rgba($secondary-color, .3);} """,
     "js": """ """,},
    
    {"html": """.wrapper
  form
    h1 Material Inputs
    h5 Inspired by Google's Material Design guidelines for text fields
    .btn-box
      a.btn.btn-link(href="https://material.google.com/components/text-fields.html" target="_blank") Design Docs
    hr.sep
    .group
      input(type="text" required)
      span.highlight
      span.bar
      label Name
    .group
      input(type="text" required)
      span.highlight
      span.bar
      label Email
    .group
      input(type="password" required)
      span.highlight
      span.bar
      label Password
    .group
      input(type="number" required)
      span.highlight
      span.bar
      label Number
    .group
      textarea(type="textarea" rows="5" required)
      span.highlight
      span.bar
      label Message
    .btn-box
      button.btn.btn-submit(type="submit") submit
      button.btn.btn-cancel(type="button") cancel
      h5 *these buttons do nothing 
        span.emoji &#x1F609; """,
     "css": """// VARIABLES // ============================== //
$bg-color: #424242;
$hl-color: #2196F3;
$muted-color: mix(white, $bg-color, 70%);
$trans-time: 300ms;
$width: 320px;

*,
:before,
:after {
  box-sizing: border-box;
}

body {
  background: $bg-color;
}

// FORM // ============================== //
form {
  width: $width;
  margin: 45px auto;
  
  h1 {
    font-size: 3em;
    font-weight: 300;
    text-align: center;
    color: $hl-color;
  }
  h5 {
    text-align: center;
    text-transform: uppercase;
    color: $muted-color;
  }
  hr.sep {
    background: $hl-color;
    box-shadow: none;
    border: none;
    height: 2px;
    width: 25%;
    margin: 0px auto 45px auto;
  }
  .emoji {
    font-size: 1.2em;
  }
}

.group {
  position: relative;
  margin: 45px 0;
}

// INPUTS // ============================== //
textarea {
  resize: none;
}

input,
textarea {
  background: none;
  color: $muted-color;
  font-size: 18px;
  padding: 10px 10px 10px 5px;
  display: block;
  width: $width;
  border: none;
  border-radius: 0;
  border-bottom: 1px solid $muted-color;
  &:focus {
    outline: none;
  }
  &:focus ~ label,
  &:valid ~ label {
    top: -14px;
    font-size: 12px;
    color: $hl-color;
  }
  &:focus ~ .bar:before {
    width: $width;
  }
}

input[type="password"] {
  letter-spacing: 0.3em;
}

label {
  color: $muted-color;
  font-size: 16px;
  font-weight: normal;
  position: absolute;
  pointer-events: none;
  left: 5px;
  top: 10px;
  transition: $trans-time ease all;
}

.bar {
  position: relative;
  display: block;
  width: $width;
  &:before {
    content: '';
    height: 2px;
    width: 0;
    bottom: 0px;
    position: absolute;
    background: $hl-color;
    transition: $trans-time ease all;
    left: 0%;
  }
}

// BUTTONS // ============================== //
.btn {
  background: #fff;
  color: mix(black, $muted-color, 25%);
  border: none;
  padding: 10px 20px;
  border-radius: 3px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  text-decoration: none;
  outline: none;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  transition: all 0.3s cubic-bezier(.25, .8, .25, 1);
  &:hover {
    color: mix(black, $muted-color, 30%);
    box-shadow: 0 7px 14px rgba(0, 0, 0, 0.18), 0 5px 5px rgba(0, 0, 0, 0.12);
  }
  &.btn-link {
    background: $hl-color;
    color: mix(white, $hl-color, 80%);
    &:hover {
      background: darken($hl-color, 5%);
      color: mix(white, $hl-color, 85%);
    }
  }
  &.btn-submit {
    background: $hl-color;
    color: mix(white, $hl-color, 70%);
    &:hover {
      background: darken($hl-color, 5%);
      color: mix(white, $hl-color, 85%);
    }
  }
  &.btn-cancel {
    background: #eee;
    &:hover {
      background: darken(#eee, 5%);
      color: mix(black, $muted-color, 30%);
    }
  }
}

.btn-box {
  text-align: center;
  margin: 50px 0;
} """,
     "js": """//not today!


//...maybe tomorrow? :) """,},
    
    {"html": """<h1>Nice input box</h1>
<form>
  <input type="text" name="name" class="question" id="nme" required autocomplete="off" />
  <label for="nme"><span>What's your name?</span></label>
  <textarea name="message" rows="2" class="question" id="msg" required autocomplete="off"></textarea>
  <label for="msg"><span>What's your message?</span></label>
  <input type="submit" value="Submit!" />
</form> """,
     "css": """/*
Basic input element using psuedo classes
*/

html {
  font-family: 'Lora', sans-serif;
  width: 100%;
}

body {
  margin: 5% auto 0 auto;
  width: 90%;
  max-width: 1125px;
}

h1 {
  font-size: 28px;
  margin-bottom: 2.5%;
}

input,
span,
label,
textarea {
  font-family: 'Ubuntu', sans-serif;
  display: block;
  margin: 10px;
  padding: 5px;
  border: none;
  font-size: 22px;
}

textarea:focus,
input:focus {
  outline: 0;
}
/* Question */

input.question,
textarea.question {
  font-size: 48px;
  font-weight: 300;
  border-radius: 2px;
  margin: 0;
  border: none;
  width: 80%;
  background: rgba(0, 0, 0, 0);
  transition: padding-top 0.2s ease, margin-top 0.2s ease;
  overflow-x: hidden; /* Hack to make "rows" attribute apply in Firefox. */
}
/* Underline and Placeholder */

input.question + label,
textarea.question + label {
  display: block;
  position: relative;
  white-space: nowrap;
  padding: 0;
  margin: 0;
  width: 10%;
  border-top: 1px solid red;
  -webkit-transition: width 0.4s ease;
  transition: width 0.4s ease;
  height: 0px;
}

input.question:focus + label,
textarea.question:focus + label {
  width: 80%;
}

input.question:focus,
input.question:valid {
  padding-top: 35px;
}

textarea.question:valid,
textarea.question:focus {
  margin-top: 35px;
}

input.question:focus + label > span,
input.question:valid + label > span {
  top: -100px;
  font-size: 22px;
  color: #333;
}

textarea.question:focus + label > span,
textarea.question:valid + label > span {
  top: -150px;
  font-size: 22px;
  color: #333;
}

input.question:valid + label,
textarea.question:valid + label {
  border-color: green;
}

input.question:invalid,
textarea.question:invalid {
  box-shadow: none;
}

input.question + label > span,
textarea.question + label > span {
  font-weight: 300;
  margin: 0;
  position: absolute;
  color: #8F8F8F;
  font-size: 48px;
  top: -66px;
  left: 0px;
  z-index: -1;
  -webkit-transition: top 0.2s ease, font-size 0.2s ease, color 0.2s ease;
  transition: top 0.2s ease, font-size 0.2s ease, color 0.2s ease;
}

input[type="submit"] {
  -webkit-transition: opacity 0.2s ease, background 0.2s ease;
  transition: opacity 0.2s ease, background 0.2s ease;
  display: block;
  opacity: 0;
  margin: 10px 0 0 0;
  padding: 10px;
  cursor: pointer;
}

input[type="submit"]:hover {
  background: #EEE;
}

input[type="submit"]:active {
  background: #999;
}

input.question:valid ~ input[type="submit"], textarea.question:valid ~ input[type="submit"] {
  -webkit-animation: appear 1s forwards;
  animation: appear 1s forwards;
}

input.question:invalid ~ input[type="submit"], textarea.question:invalid ~ input[type="submit"] {
  display: none;
}

@-webkit-keyframes appear {
  100% {
    opacity: 1;
  }
}

@keyframes appear {
  100% {
    opacity: 1;
  }
}
 """,
     "js": """ """,},
    
    {"html": """<form>
  <h1>Material Design Text Input With No Extra Markup</h1>
  <input placeholder="Username" type="text" required="">
  <input placeholder="Password" type="password" required="">
  <button>Submit</button>
</form> 

<a class="follow" href="https://twitter.com/mildrenben" target="_blank"><i class="fa fa-twitter"></i>Follow Me</a>

<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">

<link href='https://fonts.googleapis.com/css?family=Roboto:400' rel='stylesheet' type='text/css'> """,
     "css": """$color: #1abc9c;

h1, input::-webkit-input-placeholder, button {
  font-family: 'roboto', sans-serif;
  transition: all 0.3s ease-in-out;
}

h1 {
  height: 100px;
  width: 100%;
  font-size: 18px;
  background: darken($color, 4%);
  color: white;
  line-height: 150%;
  border-radius: 3px 3px 0 0;
  box-shadow: 0 2px 5px 1px rgba(0,0,0,0.2);
}

form {
  box-sizing: border-box;
  width: 260px;
  margin: 100px auto 0;
  box-shadow: 2px 2px 5px 1px rgba(0,0,0,0.2);
  padding-bottom: 40px;
  border-radius: 3px;
  h1 {
    box-sizing: border-box;
    padding: 20px;
  }
}

input {
  margin: 40px 25px;
  width: 200px;
  display: block;
  border: none;
  padding: 10px 0;
  border-bottom: solid 1px $color;
  transition: all 0.3s cubic-bezier(.64,.09,.08,1);
  background: linear-gradient(to bottom, rgba(255,255,255,0) 96%, $color 4%);
  background-position: -200px 0;
  background-size: 200px 100%;
  background-repeat: no-repeat;
  color: darken($color, 20%);
  &:focus, &:valid {
    box-shadow: none;
    outline: none;
    background-position: 0 0;
    &::-webkit-input-placeholder {
      color: $color;
      font-size: 11px;
      transform: translateY(-20px);
      visibility: visible !important;
    }
  }
}

button {
  border: none;
  background: $color;
  cursor: pointer;
  border-radius: 3px;
  padding: 6px;
  width: 200px;
  color: white;
  margin-left: 25px;
  box-shadow: 0 3px 6px 0 rgba(0,0,0,0.2);
  &:hover { 
    transform: translateY(-3px);
    box-shadow: 0 6px 6px 0 rgba(0,0,0,0.2);
  }
}

.follow {
  width: 42px;
  height: 42px;
  border-radius: 50px;
  background: #03A9F4;
  display: inline-block;
  margin: 50px calc(50% - 21px);
  white-space: nowrap;
  padding: 13px;
  box-sizing: border-box;
  color: white;
  transition: all 0.2s ease;
  font-family: Roboto, sans-serif;
  text-decoration: none;
  box-shadow: 0 5px 6px 0 rgba(0,0,0,0.2);
  i {
    margin-right: 20px;
    transition: margin-right 0.2s ease;
  }
  &:hover {
    width: 134px;
    transform: translateX(-50px);
    i {
      margin-right: 10px;
    }
  }
} """,
     "js": """ """,},
    
    {"html": """<div class="container">
  
  <h2>Google Material Design in CSS3<small>Inputs</small></h2>
  
  <form>
    
    <div class="group">      
      <input type="text" required>
      <span class="highlight"></span>
      <span class="bar"></span>
      <label>Name</label>
    </div>
      
    <div class="group">      
      <input type="text" required>
      <span class="highlight"></span>
      <span class="bar"></span>
      <label>Email</label>
    </div>
    
  </form>
      
  <p class="footer">
    a <a href="https://scotch.io/tutorials/css/google-material-design-input-boxes-in-css3" target="_blank">tutorial</a> by <a href="https://scotch.io" target="_blank">scotch.io</a>
  </p>
  
</div> """,
     "css": """* { box-sizing:border-box; }

/* basic stylings ------------------------------------------ */
body 				 { background:url(https://scotch.io/wp-content/uploads/2014/07/61.jpg); }
.container 		{ 
  font-family:'Roboto';
  width:600px; 
  margin:30px auto 0; 
  display:block; 
  background:#FFF;
  padding:10px 50px 50px;
}
h2 		 { 
  text-align:center; 
  margin-bottom:50px; 
}
h2 small { 
  font-weight:normal; 
  color:#888; 
  display:block; 
}
.footer 	{ text-align:center; }
.footer a  { color:#53B2C8; }

/* form starting stylings ------------------------------- */
.group 			  { 
  position:relative; 
  margin-bottom:45px; 
}
input 				{
  font-size:18px;
  padding:10px 10px 10px 5px;
  display:block;
  width:300px;
  border:none;
  border-bottom:1px solid #757575;
}
input:focus 		{ outline:none; }

/* LABEL ======================================= */
label 				 {
  color:#999; 
  font-size:18px;
  font-weight:normal;
  position:absolute;
  pointer-events:none;
  left:5px;
  top:10px;
  transition:0.2s ease all; 
  -moz-transition:0.2s ease all; 
  -webkit-transition:0.2s ease all;
}

/* active state */
input:focus ~ label, input:valid ~ label 		{
  top:-20px;
  font-size:14px;
  color:#5264AE;
}

/* BOTTOM BARS ================================= */
.bar 	{ position:relative; display:block; width:300px; }
.bar:before, .bar:after 	{
  content:'';
  height:2px; 
  width:0;
  bottom:1px; 
  position:absolute;
  background:#5264AE; 
  transition:0.2s ease all; 
  -moz-transition:0.2s ease all; 
  -webkit-transition:0.2s ease all;
}
.bar:before {
  left:50%;
}
.bar:after {
  right:50%; 
}

/* active state */
input:focus ~ .bar:before, input:focus ~ .bar:after {
  width:50%;
}

/* HIGHLIGHTER ================================== */
.highlight {
  position:absolute;
  height:60%; 
  width:100px; 
  top:25%; 
  left:0;
  pointer-events:none;
  opacity:0.5;
}

/* active state */
input:focus ~ .highlight {
  -webkit-animation:inputHighlighter 0.3s ease;
  -moz-animation:inputHighlighter 0.3s ease;
  animation:inputHighlighter 0.3s ease;
}

/* ANIMATIONS ================ */
@-webkit-keyframes inputHighlighter {
	from { background:#5264AE; }
  to 	{ width:0; background:transparent; }
}
@-moz-keyframes inputHighlighter {
	from { background:#5264AE; }
  to 	{ width:0; background:transparent; }
}
@keyframes inputHighlighter {
	from { background:#5264AE; }
  to 	{ width:0; background:transparent; }
} """,
     "js": """ """,},
    
    {"html": """<div class="container">
  
  <h2>Google Material Design in CSS3<small>Inputs</small></h2>
  
  <form>
    
    <div class="group">      
      <input type="text" required>
      <span class="highlight"></span>
      <span class="bar"></span>
      <label>Name</label>
    </div>
      
    <div class="group">      
      <input type="text" required>
      <span class="highlight"></span>
      <span class="bar"></span>
      <label>Email</label>
    </div>
    
  </form>
      
  <p class="footer">
    a <a href="https://scotch.io/tutorials/css/google-material-design-input-boxes-in-css3" target="_blank">tutorial</a> by <a href="https://scotch.io" target="_blank">scotch.io</a>
  </p>
  
</div> """,
     "css": """* { box-sizing:border-box; }

/* basic stylings ------------------------------------------ */
body 				 { background:url(https://scotch.io/wp-content/uploads/2014/07/61.jpg); }
.container 		{ 
  font-family:'Roboto';
  width:600px; 
  margin:30px auto 0; 
  display:block; 
  background:#FFF;
  padding:10px 50px 50px;
}
h2 		 { 
  text-align:center; 
  margin-bottom:50px; 
}
h2 small { 
  font-weight:normal; 
  color:#888; 
  display:block; 
}
.footer 	{ text-align:center; }
.footer a  { color:#53B2C8; }

/* form starting stylings ------------------------------- */
.group 			  { 
  position:relative; 
  margin-bottom:45px; 
}
input 				{
  font-size:18px;
  padding:10px 10px 10px 5px;
  display:block;
  width:300px;
  border:none;
  border-bottom:1px solid #757575;
}
input:focus 		{ outline:none; }

/* LABEL ======================================= */
label 				 {
  color:#999; 
  font-size:18px;
  font-weight:normal;
  position:absolute;
  pointer-events:none;
  left:5px;
  top:10px;
  transition:0.2s ease all; 
  -moz-transition:0.2s ease all; 
  -webkit-transition:0.2s ease all;
}

/* active state */
input:focus ~ label, input:valid ~ label 		{
  top:-20px;
  font-size:14px;
  color:#5264AE;
}

/* BOTTOM BARS ================================= */
.bar 	{ position:relative; display:block; width:300px; }
.bar:before, .bar:after 	{
  content:'';
  height:2px; 
  width:0;
  bottom:1px; 
  position:absolute;
  background:#5264AE; 
  transition:0.2s ease all; 
  -moz-transition:0.2s ease all; 
  -webkit-transition:0.2s ease all;
}
.bar:before {
  left:50%;
}
.bar:after {
  right:50%; 
}

/* active state */
input:focus ~ .bar:before, input:focus ~ .bar:after {
  width:50%;
}

/* HIGHLIGHTER ================================== */
.highlight {
  position:absolute;
  height:60%; 
  width:100px; 
  top:25%; 
  left:0;
  pointer-events:none;
  opacity:0.5;
}

/* active state */
input:focus ~ .highlight {
  -webkit-animation:inputHighlighter 0.3s ease;
  -moz-animation:inputHighlighter 0.3s ease;
  animation:inputHighlighter 0.3s ease;
}

/* ANIMATIONS ================ */
@-webkit-keyframes inputHighlighter {
	from { background:#5264AE; }
  to 	{ width:0; background:transparent; }
}
@-moz-keyframes inputHighlighter {
	from { background:#5264AE; }
  to 	{ width:0; background:transparent; }
}
@keyframes inputHighlighter {
	from { background:#5264AE; }
  to 	{ width:0; background:transparent; }
} """,
     "js": """ """,},
    
    {"html": """<form>
  <h1>Fancy Text Inputs</h1>
  <div class="question">
    <input type="text" required/>
    <label>First Name</label>
  </div>
  <div class="question">
    <input type="text" required/>
    <label>Last Name</label>
  </div>
  <div class="question">
    <input type="text" required/>
    <label>Email Address</label>
  </div>
  <div class="question">
    <input type="text" required/>
    <label>Email Confirm</label>
  </div>
  <button>Submit</button>
</form> """,
     "css": """@import compass

$red: rgba(255,74,86,1)
.transition
  @include transition( all 0.25s cubic-bezier(.53,.01,.35,1.5))

*
  font-family: Helvetica , sans-serif
  font-weight: light
  -webkit-font-smoothing: antialiased
    
html
  background-color: $red //rgba(245,248,252,1)

form
  position: relative
  display: inline-block
  max-width: 700px
  min-width: 500px
  box-sizing: border-box
  padding: 30px 25px
  background-color: white
  border-radius: 40px
  margin: 40px 0
  left: 50%
  @include translate( -50% , 0 )
    
  h1
    color: $red
    font-weight: 100
    letter-spacing: 0.01em
    margin-left: 15px
    margin-bottom: 35px
    text-transform: uppercase
      
  button
    @extend .transition
    margin-top: 35px
    background-color: white
    border: 1px solid $red
    line-height: 0
    font-size: 17px
    display: inline-block
    box-sizing: border-box
    padding: 20px 15px 
    border-radius: 60px
    color: $red
    font-weight: 100
    letter-spacing: 0.01em
    position: relative
    z-index: 1
    
    &:hover , &:focus
      color: white
      background-color: $red
    
  .question
    position: relative
    padding: 10px 0
    
    &:first-of-type
      padding-top: 0
      
    &:last-of-type
      padding-bottom: 0
      
    label
      @extend .transition
      transform-origin: left center
      color: $red
      font-weight: 100
      letter-spacing: 0.01em
      font-size: 17px
      box-sizing: border-box
      padding: 10px 15px
      display: block
      position: absolute
      margin-top: -40px
      z-index: 2
      pointer-events: none
      
    input[type="text"]
      @extend .transition
      appearance: none
      background-color: none
      border: 1px solid $red
      line-height: 0
      font-size: 17px
      width: 100%
      display: block
      box-sizing: border-box
      padding: 10px 15px
      border-radius: 60px
      color: $red
      font-weight: 100
      letter-spacing: 0.01em
      position: relative
      z-index: 1
      
      &:focus
        outline: none
        background: $red
        color: white
        margin-top: 30px
        
      &:valid
        margin-top: 30px
          
      &:focus ~ label
        @include translate( 0 , -35px )
      
      &:valid ~ label
        text-transform: uppercase
        font-style: italic
        @include transform( translate( 5px , -35px ) scale(0.6)) """,
     "js": """ """,},
    
    {"html": """<div class="row">
  <p>Click every input.</p>
</div>
<div class="row">
  <span>
    <input class="basic-slide" id="name" type="text" placeholder="Your best name" /><label for="name">Name</label>
  </span>
  <span>
    <input class="basic-slide" id="email" type="text" placeholder="Your favorite email" /><label for="email">Email</label>
  </span>
  <span>
    <input class="basic-slide" id="phone" type="text" placeholder="You can trust us" /><label for="phone">Phone</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="clean-slide" id="age" type="text" placeholder="Go for the high score!" /><label for="age">Age</label>
  </span>
  <span>
    <input class="clean-slide" id="height" type="text" placeholder="Heels count" /><label for="height">Height</label>
  </span>
  <span>
    <input class="clean-slide" id="weight" type="text" placeholder="Go ahead and lie" /><label for="weight">Weight</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="gate" id="class" type="text" placeholder="Wizard!" /><label for="class">Class</label>
  </span>
  <span>
    <input class="gate" id="element" type="text" placeholder="Five to choose from" /><label for="element">Element</label>
  </span>
  <span>
    <input class="gate" id="move" type="text" placeholder="Secret book attack!" /><label for="move">Move</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="skinny" id="english" type="text" placeholder="Do you speak it?" /><label for="english">English</label>
  </span>
  <span>
    <input class="skinny" id="burger" type="text" placeholder="A Royale with cheese?" /><label for="burger">Burger</label>
  </span>
  <span>
    <input class="skinny" id="wallet" type="text" placeholder="Bad Mother****er" /><label for="wallet">Wallet</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="slide-up" id="card" type="text" placeholder="Fund me!" /><label for="card">Credit Card</label>
  </span>
  <span>
    <input class="slide-up" id="expires" type="text" placeholder="Month Day, Year" /><label for="expires">Expires</label>
  </span>
  <span>
    <input class="slide-up" id="security" type="text" placeholder="Public" /><label for="security">Security Code</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="card-slide" id="knock" type="text" placeholder="Who's there?" /><label for="knock">Knock knock</label>
  </span>
  <span>
    <input class="card-slide" id="max" type="text" placeholder="Max who?" /><label for="max">Max</label>
  </span>
  <span>
    <input class="card-slide" id="out" type="text" placeholder="Sunuva..." /><label for="out">Maxed out card ;)</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="swing" id="artist" type="text" placeholder="BO$$" /><label for="artist">Artist</label>
  </span>
  <span>
    <input class="swing" id="song" type="text" placeholder="I don't give a ****" /><label for="song">Song</label>
  </span>
  <span>
    <input class="swing" id="eyes" type="text" placeholder="Crazy" /><label for="eyes">Eyes</label>
  </span>
</div>
<div class="row">
  <span>
    <input class="balloon" id="state" type="text" placeholder="Liquid, solid, gaseous..." /><label for="state">State</label>
  </span>
  <span>
    <input class="balloon" id="planet" type="text" placeholder="Probably Earth" /><label for="planet">Planet</label>
  </span>
  <span>
    <input class="balloon" id="galaxy" type="text" placeholder="Milky Way?" /><label for="galaxy">Galaxy</label>
  </span>
</div> """,
     "css": """@import "compass/css3";

@import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700,600,300,800);

* {
  box-sizing: border-box;
}
html,
body {
  overflow-x: hidden;
  font-family: "Open Sans", sans-serif;
  font-weight: 300;
  line-height: 1.4;
  color: #fff;
  background: #efefef;
}
@mixin epic-sides() { // https://codepen.io/MichaelArestad/pen/qltuk
    position: relative;
    z-index: 1;

    &:before {
        position: absolute;
        content: "";
        display: block;
        top: 0;
        left: -5000px;
        height: 100%;
        width: 15000px;
        z-index: -1;
        @content;
    }
}
.row {
  max-width: 800px;
  margin: 0 auto;
  padding: 60px 30px;
  background: #032429;
  @include epic-sides() {background: inherit;}
  text-align: center;
  
  &:first-child {
    padding: 40px 30px;
  }
  &:nth-child(2),
  &:nth-child(8),
  &:nth-child(10){
    background: #134A46;
  }
  &:nth-child(3),
  &:nth-child(7) {
    background: #377D6A;
  }
  &:nth-child(4),
  &:nth-child(6) {
    background: #7AB893;
  }
  &:nth-child(5) {
    background: #B2E3AF;
  }
  
  span {
    position: relative;
    display: inline-block;
    margin: 30px 10px;
  }
}
.basic-slide {
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 70px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    padding: 10px 15px;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    background: #7AB893;
    transition: all .3s ease-in-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
  }
}
.basic-slide:focus,
.basic-slide:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    transform: translateX(-100%);
  }
}
.clean-slide {
  position: relative;
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 60px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    transform: translateX(0);
    top: 0;
    left: 0;
    bottom: 0;
    padding: 13px 15px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #032429;
    text-align: left;
    text-shadow: 0 1px 0 rgba(255,255,255,.4);
    transition: all .3s ease-in-out, color .3s ease-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    overflow: hidden;
    
    &:after {
      content: "";
      position: absolute;
      top: 0;
      right: 100%;
      bottom: 0;
      width: 100%;
      background: #7AB893;
      z-index: -1;
      transform: translate(0);
      transition: all .3s ease-in-out;
      border-top-left-radius: 3px;
      border-bottom-left-radius: 3px;
    }
  }
}
.clean-slide:focus,
.clean-slide:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    color: #fff;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    transform: translateX(-100%);
    
    &:after {
      transform: translate(100%);
    }
  }
}
.gate {
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 65px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 15px;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    background: #7AB893;
    transition: all .4s ease-in-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    transform-origin: left bottom;
    z-index: 99;
    
    &:before,
    &:after {
      content: "";
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      border-radius: 3px;
      background: #377D6A;
      transform-origin: left bottom;
      transition: all .4s ease-in-out;
      pointer-events: none;
      z-index: -1;
    }
    &:before {
      background: rgba(3,36,41,.2);
      z-index: -2;
      right: 20%;
    }
  }
}
span:nth-child(2) .gate {
  text-indent: 85px;
}
span:nth-child(2) .gate:focus,
span:nth-child(2) .gate:active{
  text-indent: 0;
}
.gate:focus,
.gate:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    transform: rotate(-66deg);
    border-radius: 3px;
    
    &:before {
      transform: rotate(10deg);
    }
  }
}
.skinny {
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 75px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    transform: translateX(0);
    top: 0;
    left: 0;
    padding: 10px 15px;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    transition: all .3s ease-in-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    overflow: hidden;

    &:before,
    &:after {
      content: "";
      position: absolute;
      right: 0;
      left: 0;
      z-index: -1;
      transition: all .3s ease-in-out;
    }
    &:before {
      // Skinny bit here
      top: 5px;
      bottom: 5px;
      background: #377D6A; // change this to #134A46
      border-top-left-radius: 3px;
      border-bottom-left-radius: 3px;
    }
    &:after {
      top: 0;
      bottom: 0;
      background: #377D6A;
    }
  }
}
.skinny:focus,
.skinny:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    transform: translateX(-100%);
    
    &:after {
      transform: translateX(100%);
    }
  }
}
.slide-up {
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 80px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    transform: translateX(0);
    top: 0;
    left: 0;
    padding: 10px 15px;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    transition: all .3s ease-in-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    overflow: hidden;

    &:before,
    &:after {
      content: "";
      position: absolute;
      right: 0;
      left: 0;
      z-index: -1;
      transition: all .3s ease-in-out;
    }
    &:before {
      // Skinny bit here
      top: 6px;
      left: 5px;
      right: 5px;
      bottom: 6px;
      background: #377D6A; // change this to #134A46
    }
    &:after {
      top: 0;
      bottom: 0;
      background: #377D6A;
    }
  }
}
span:nth-child(1) .slide-up {
  text-indent: 105px;
}
span:nth-child(3) .slide-up {
  text-indent: 125px;
}
span:nth-child(1) .slide-up:focus,
span:nth-child(1) .slide-up:active,
span:nth-child(3) .slide-up:focus,
span:nth-child(3) .slide-up:active {
  text-indent: 0;
}
.slide-up:focus,
.slide-up:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    transform: translateY(-100%);

    &:before {
      border-radius: 5px;
    }
    &:after {
      transform: translateY(100%);
    }
  }
}
.card-slide {
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 115px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 15px;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    background: #7AB893;
    transition: all .3s ease-in-out;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    transform-origin: right center;
    transform: perspective(300px) scaleX(1) rotateY(0deg);
  }
}
span:nth-child(2) .card-slide {
  text-indent: 55px;
}
span:nth-child(3) .card-slide {
  text-indent: 150px;
}
span:nth-child(2) .card-slide:focus,
span:nth-child(2) .card-slide:active,
span:nth-child(3) .card-slide:focus,
span:nth-child(3) .card-slide:active {
  text-indent: 0;
}
.card-slide:focus,
.card-slide:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    transform: perspective(600px) translateX(-100%) rotateY(80deg);
  }
}
.swing {
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 60px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 15px;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    background: #7AB893;
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    transform-origin: 2px 2px;
    transform: rotate(0);
    // There should be a better way
    animation: swing-back .4s 1 ease-in-out;
  }
}
@keyframes swing {
  0% {
    transform: rotate(0);
  }
  20% {
    transform: rotate(116deg);
  }
  40% {
    transform: rotate(60deg);
  }
  60% {
    transform: rotate(98deg);
  }
  80% {
    transform: rotate(76deg);
  }
  100% {
    transform: rotate(82deg);
  }
}
@keyframes swing-back {
  0% {
    transform: rotate(82deg);
  }
  100% {
    transform: rotate(0);
  }
}
.swing:focus,
.swing:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    animation: swing 1.4s 1 ease-in-out;
    transform: rotate(82deg);
  }
}
.balloon {
  // As suggested by https://twitter.com/dbox/status/365888496486985728
  display: inline-block;
  width: 215px;
  padding: 10px 0 10px 15px;
  font-family: "Open Sans", sans;
  font-weight: 400;
  color: #377D6A;
  background: #efefef;
  border: 0;
  border-radius: 3px;
  outline: 0;
  text-indent: 60px; // Arbitrary.
  transition: all .3s ease-in-out;
  
  &::-webkit-input-placeholder {
    color: #efefef;
    text-indent: 0;
    font-weight: 300;
  }

  + label {
    display: inline-block;
    position: absolute;
    top: 8px;
    left: 0;
    bottom: 8px;
    padding: 5px 15px;
    color: #032429;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    text-shadow: 0 1px 0 rgba(19,74,70,0);
    transition: all .3s ease-in-out;
    border-radius: 3px;
    background: rgba(122,184,147,0);
    
    &:after {
      position: absolute;
      content: "";
      width: 0;
      height: 0;
      top: 100%;
      left: 50%;
      margin-left: -3px;
      border-left: 3px solid transparent;
      border-right: 3px solid transparent;
      border-top: 3px solid rgba(122,184,147,0);
      transition: all .3s ease-in-out;
    }
  }
}
.balloon:focus,
.balloon:active {
  color: #377D6A;
  text-indent: 0;
  background: #fff;
  
  &::-webkit-input-placeholder {
    color: #aaa;
  }
  + label {
    color: #fff;
    text-shadow: 0 1px 0 rgba(19,74,70,.4);
    background: rgba(122,184,147,1);
    transform: translateY(-40px);
    
    &:after {
      border-top: 4px solid rgba(122,184,147,1);
    }
  }
} """,
     "js": """ """,},
    
    {"html": """<div class="text-input">
  <input type="text" id="input1" placeholder="Try typing something in here!">
  <label for="input1">Name</label>
</div> """,
     "css": """@import  url(https://fonts.googleapis.com/css?family=Montserrat);

body{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-family: Montserrat;
  background: #313E50;
}

.text-input{
  
  position: relative;
  margin-top: 50px;
  
  input[type="text"]{
    display: inline-block;
    width: 500px;
    height: 40px;
    box-sizing: border-box;
    outline: none;
    border: 1px solid lightgray;
    border-radius: 3px;
    padding: 10px 10px 10px 100px;
    transition: all 0.1s ease-out;
  }
  
  input[type="text"] + label{
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    height: 40px;
    line-height: 40px;
    color: white;
    border-radius: 3px 0 0 3px;
    padding: 0 20px;
    background: #E03616;
    transform: translateZ(0) translateX(0);
    transition: all 0.3s ease-in;
    transition-delay: 0.2s;
  }
  
  input[type="text"]:focus + label{
    transform: translateY(-120%) translateX(0%);
    border-radius: 3px;
    transition: all 0.1s ease-out;
  }
  
  input[type="text"]:focus{
    padding: 10px;
    transition: all 0.3s ease-out;
    transition-delay: 0.2s;
  }
} """,
     "js": """ """,},
    
    {"html": """<!--  
View the step by step video tutorial on how to create this login form with only css(sass) and html

https://youtu.be/dok2xAaheWk
-->

<div class="wrapper">
        <div class="container">
            <div class="tabs">
                <!-- Sign In -->
                <input type="radio" class="tabs__button" name="signForm" id="signIn" checked />
                <label class="tabs__text" for="signIn">Sign In</label>
                <div class="tabs__content">
                    <h1>Welcome back!</h1>
                    <p>Get back on your track</p>
                    <form class="form">
                        <div class="input-group">
                            <input class="input-group__input" type="text" placeholder="&nbsp;" name="username" id="username" autocomplete="off" required />
                            <label class="input-group__label" for="username">Username</label>
                        </div>
                        <div class="input-group">
                            <input class="input-group__input" type="password" name="password" placeholder="&nbsp;" id="password" required />
                            <label class="input-group__label" for="password">Password</label>
                        </div>
                        <!-- Normally I would create a grid system or use an existing to cater this issue -->
                        <div class="flex-space-between">
                            <label class="flex-align-center"><input type="checkbox" /> Remember Me</label>
                            <p><a href="#">Forgot Password?</a></p>
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </div>

                <!-- Sign Up -->
                <input type="radio" class="tabs__button" name="signForm" id="signUp" />
                <label class="tabs__text" for="signUp">Sign Up</label>
                <div class="tabs__content">
                    <h1>New Account</h1>
                    <p>Start your journey now</p>
                    <form class="form">
                        <div class="input-group">
                            <input class="input-group__input" type="email" placeholder="&nbsp;" name="username" id="username" autocomplete="off" required />
                            <label class="input-group__label" for="email">Email</label>
                        </div>
                        <div class="input-group">
                            <input class="input-group__input" type="password" name="password" placeholder="&nbsp;" id="password" required />
                            <label class="input-group__label" for="password">Password</label>
                        </div> 
                        <p><small>By submitting this form, you confirm you have read and agreed to the <a href="#">Terms and Conditions.</a></small></p>
                        <button type="submit">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div> """,
     "css": """@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');

// Color
$gray: #999999;
$dark-gray: #333333;
$blue: #0086e4;

$primary-color: $blue;
$border-color: #dddddd;

// Font
$primary-font: 'Lato', sans-serif;

// Typography
$body-font-family: $primary-font;
$body-font-size: 14px;
$body-color: $dark-gray;

// Input
$input-height: 40px;

// Button
$button-height: $input-height;

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  font: {
    family: $body-font-family;
    size: $body-font-size;
  }
  color: $body-color;
}

h1,
p {
  margin-top: 0;
}

h1 {
  margin-bottom: 10px;
  + p {
    color: $gray;
    margin-bottom: 30px;
  }
}

p {
  margin-bottom: 20px; 
}

a {
  color: $primary-color;
  text-decoration: none;
}

input[type="checkbox"] {
  margin: 0;
  padding: 0;
  height: 17px;
}

.wrapper {
  min-height: 100vh;
  display: grid;
  place-items: center;
  // display: flex;
  // align-items: center;
  // justify-content: center;
  background: rgb(150,0,150);
  background: linear-gradient(225deg, rgba(150,0,150,1) 0%, rgba(107,36,205,1) 50%, rgba(0,104,255,1) 100%);
}

.container {
  width: 100%;
  height: auto;
  max-width: 400px;
  min-width: 320px;
  background-color: white;
}


// Util
// You can create a different file to store all utilities classes
.flex-space-between {
  display: flex;
  justify-content: space-between;
}

.flex-align-center {
  display: flex;
  justify-content: center;
  gap: 5px;
}

button {
    cursor: pointer;
    background-color: $primary-color;
    color: white;
    border: none;
    font-weight: bold;
    text-transform: uppercase;
    border-radius: 6px;
    letter-spacing: 1px;
    width: 100%;
    height: $button-height;
    transition: 300ms background-color ease-in-out;
    &:hover {
        background-color: lighten($primary-color, 10%);
    }
}

.input-group {
    margin-bottom: 20px;
    position: relative;
    &__label {
        display: block;
        position: absolute;
        top: 0;
        // to keep the position center
        line-height: $input-height;
        color: #aaa;
        left: 5px;
        padding: 0 5px;
        transition: line-height 200ms ease-in-out,
            font-size 200ms ease-in-out, 
            top 200ms ease-in-out;
        // firefox fix
        pointer-events: none;
    }
    &__input {
        width: 100%;
        height: $input-height;
        border: 1px solid $border-color;
        border-radius: 3px;
        padding: 0 10px;
        // there must a required prop in input
        // &:valid,
        // need to add placeholder
        &:not(:placeholder-shown),
        &:focus {
            + label {
                background-color: white;
                line-height: 10px;
                opacity: 1;
                font-size: 10px;
                top: -5px;
            }
        }
        &:focus {
            outline: none;
            border: 1px solid $primary-color;
            + label {
                color: $primary-color;
            }
        }
    }
}

.tabs {
    $parent: &;
    display: flex;
    flex-flow: row wrap;
    &__text {
        flex: 1;
        margin: 0;
        cursor: pointer;
        padding: 20px 30px;
        font-size: 1.2em;
        opacity: 0.5;
        background-color: #eeeeee;
        border-top: 3px solid #eeeeee;
        transition: border-top 300ms ease-out;
        transform-origin: top;
        text-transform: uppercase;
        font-weight: bold;
        text-align: center;
    }
    &__content {
        display: none;
        flex: 1 1 100%;
        order: 99;
        padding: 40px 30px 30px 30px;
    }
    &__button {
        visibility: hidden;
        height: 0;
        margin: 0;
        position: absolute;
        &:checked {
            + #{$parent}__text {
                // order: -1;
                color: $primary-color;
                opacity: 1;
                background-color: white;
                border-top: 3px solid $primary-color;
            }
            + #{$parent}__text + #{$parent}__content {
                display: block;
            }
        }
    }
} """,
     "js": """ """,},
    
    {"html": """<div class="container">
  <div class="aks-input-row">
    <input class="aks-input" type="text" id="name" name="name" placeholder="Name...">
  </div>
  <div class="aks-input-row">
    <div class="aks-date-row">
      <input class="aks-input" type="date" id="date" name="date" placeholder="Name...">
      <div class="aks-date-calender">
        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" shape-rendering="geometricPrecision">
          <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
          <path d="M16 2v4" />
          <path d="M8 2v4" />
          <path d="M3 10h18" /></svg>
      </div>
    </div>
  </div>
  <div class="aks-input-row">
    <div class="aks-input-icon-wrap">
      <div class="aks-input-icon">
        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" shape-rendering="geometricPrecision">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
          <path d="M22 6l-10 7L2 6"></path>
        </svg>
      </div>
      <input class="aks-input" type="text" id="name" name="name" placeholder="Name...">
    </div>
  </div>
  <div class="aks-input-row">
    <div class="aks-input-wrap">
      <label class="aks-input-label" for="surname">Surname</label>
      <input class="aks-input" type="text" id="surname" name="surname" placeholder="Surname...">
    </div>
  </div>
  <div class="aks-input-row">
    <div class="aks-select-row">
      <select class="aks-input" name="select" id="select">
        <option value="Option 1" selected>Option 1</option>
        <option value="Option 2">Option 2</option>
        <option value="Option 3">Option 3</option>
        <option value="Option 4">Option 4</option>
      </select>
      <div class="aks-select-arrow"><svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" shape-rendering="geometricPrecision">
          <path d="M6 9l6 6 6-6"></path>
        </svg> </div>
    </div>
  </div>
  <div class="aks-input-row" data-password="">
    <input class="aks-input" type="password" id="password" name="password" placeholder="Password..." data-pass-target="" />
    <button class="password-show-hide" data-pass-show-hide="">

      <svg data-pass-show="" class="password-show" viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" shape-rendering="geometricPrecision">
        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
        <circle cx="12" cy="12" r="3" /></svg>
      <svg data-pass-hide="" class="password-hide" viewBox="0 0 24 24" width="18" height="18ccccc" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" shape-rendering="geometricPrecision">
        <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24" />
        <path d="M1 1l22 22" /></svg>

    </button>
  </div>
  <div class="aks-input-row">
    <input class="aks-input" type="checkbox" id="checkbox" name="checkbox">
    <label class="aks-input-label" for="checkbox">Checkbox</label>
  </div>
  <div class="aks-input-row">
    <input class="aks-input" type="radio" id="radio1" name="radio">
    <label class="aks-input-label" for="radio1">Radio</label>
  </div>
  <div class="aks-input-row">
    <input class="aks-input" type="radio" id="radio2" name="radio">
    <label class="aks-input-label" for="radio2">Radio</label>
  </div>
  <div class="aks-input-row">
    <input class="aks-switch" type="checkbox" id="switch" name="switch">
    <label class="aks-input-label" for="switch">Switch</label>
  </div>
  <div class="aks-input-row">
    <input class="aks-input" type="submit" id="submit" name="submit">
  </div>
</div> """,
     "css": """@import url("https://fonts.googleapis.com/css2?family=Inter&display=swap");
body {
  margin: 0;
  padding: 0;
  font-family: "Inter", sans-serif;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  height: 100vh;
}
.container {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
  padding-top: 2rem;
}
.aks-input-row {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  width: 100%;
  height: auto;
  position: relative;
}
.aks-input-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: auto;
  position: relative;
}
.aks-input-icon-wrap .aks-input[type="text"] {
  padding-left: 33px;
}
.aks-input-icon {
  position: absolute;
  left: 10px;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7575a0;
}
.aks-input-label {
  margin-left: 0.4rem;
  cursor: pointer;
  position: relative;
}
.aks-input-wrap .aks-input-label {
  margin-left: 0rem;
  margin-bottom: 0.3rem;
  display: block;
  font-size: 15px;
  color: #5e6272;
}
.aks-input[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  height: 21px;
  width: 21px;
  border-radius: 7px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="checkbox"]:hover {
  border-color: #275efe;
}
.aks-input[type="checkbox"]:after {
  content: "";
  display: flex;
  align-items: center;
  justify-content: center;
  width: 5px;
  height: 8px;
  border: 2px solid #fff;
  border-top: 0;
  border-left: 0;
  top: 3px;
  position: absolute;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="checkbox"]:checked {
  background: #05f;
  border: 1px solid #05f;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="checkbox"]:checked:after {
  -webkit-transform: rotate(43deg);
  transform: rotate(43deg);
}
.aks-input[type="checkbox"]:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-input[type="checkbox"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.aks-input[type="radio"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  height: 21px;
  width: 21px;
  border-radius: 9999px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="radio"]:hover {
  border-color: #275efe;
}
.aks-input[type="radio"]:after {
  content: "";
  width: 19px;
  height: 19px;
  position: absolute;
  border-radius: 9999px;
  background: #fff;
  opacity: 0;
  -webkit-transform: scale(0.7);
  transform: scale(0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="radio"]:checked {
  background: #05f;
  border: 1px solid #05f;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="radio"]:checked:after {
  -webkit-transform: scale(0.5);
  transform: scale(0.5);
  opacity: 1;
}
.aks-input[type="radio"]:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-input[type="radio"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.aks-switch[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  height: 21px;
  width: 38px;
  border-radius: 11px;
  outline: none;
  display: flex;
  align-items: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-switch[type="checkbox"]:hover {
  border-color: #275efe;
}
.aks-switch[type="checkbox"]:after {
  content: "";
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 9999px;
  width: 13px;
  height: 13px;
  background: #bbc1e1;
  -webkit-transform: translateX(0);
  transform: translateX(0);
  position: absolute;
  left: 2px;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-switch[type="checkbox"]:checked {
  background: #05f;
  border: 1px solid #05f;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-switch[type="checkbox"]:checked:after {
  -webkit-transform: translateX(17px);
  transform: translateX(17px);
  background: white;
}
.aks-switch[type="checkbox"]:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-switch[type="checkbox"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.aks-input[type="text"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  border-radius: 7px;
  padding: 8px 10px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="text"]:hover {
  border-color: #275efe;
}
.aks-input[type="text"]:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-input[type="text"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.aks-input[type="password"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  border-radius: 7px;
  padding: 8px 10px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="password"]:hover {
  border-color: #275efe;
}
.aks-input[type="password"]:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-input[type="password"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.password-show-hide {
  position: absolute;
  right: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  z-index: 1;
  color: #7575a0;
  cursor: pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  width: fit-content;
  border: none;
  background: transparent;
  padding: 0;
  margin: 0;
  outline: none;
}
.password-show-hide:hover {
  color: #275efe;
}
.password-show-hide:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  color: #275efe;
}

.aks-select-row {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
}
.aks-select-arrow {
  position: absolute;
  right: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
select.aks-input {
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  border-radius: 7px;
  padding: 8px 10px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  color: #6d6d6d;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
select.aks-input:hover {
  border-color: #275efe;
}
select.aks-input:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
select.aks-input:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.aks-input[type="submit"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  border-radius: 7px;
  padding: 8px 10px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #275efe;
  background: #275efe;
  color: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="submit"]:hover {
  border-color: #275efe;
}
.aks-input[type="submit"]:focus {
  box-shadow: 0 0 0 3px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-input[type="submit"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}

.aks-date-row {
  width: 100%;
  display: flex;
  align-items: center;
  position: relative;
}
.aks-date-calender {
  position: absolute;
  right: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  z-index: 1;
  color: #7575a0;
  cursor: pointer;
}
.aks-date-calender:hover {
  color: #275efe;
}
.aks-input[type="date"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  border-radius: 7px;
  padding: 8px 10px;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: unset;
  position: relative;
  margin: 0;
  cursor: pointer;
  border: 0.1rem solid #bbc1e1;
  background: #fff;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.aks-input[type="date"]:hover {
  border-color: #275efe;
}
.aks-input[type="date"]:focus {
  box-shadow: 0 0 0 2px rgba(39, 94, 254, 0.3);
  border-color: #275efe;
}
.aks-input[type="date"]:disabled {
  background: #f6f8ff;
  cursor: not-allowed;
  opacity: 0.9;
  border-color: #bbc1e1;
}
.aks-input[type="date"]::-webkit-inner-spin-button {
  display: none;
}
.aks-input[type="date"]::-webkit-calendar-picker-indicator {
  position: absolute;
  right: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  z-index: 5;
  color: #7575a0;
  cursor: pointer;
  opacity: 0;
}
 """,
     "js": """(function () {
  "use strict";
  var jQueryPlugin = (window.jQueryPlugin = function (ident, func) {
    return function (arg) {
      if (this.length > 1) {
        this.each(function () {
          var $this = $(this);

          if (!$this.data(ident)) {
            $this.data(ident, func($this, arg));
          }
        });

        return this;
      } else if (this.length === 1) {
        if (!this.data(ident)) {
          this.data(ident, func(this, arg));
        }

        return this.data(ident);
      }
    };
  });
})();

(function () {
  "use strict";
  function Pass_Show_Hide($root) {
    const element = $root;
    const pass_target = $root.first("data-password");
    const pass_elemet = $root.find("[data-pass-target]");
    const pass_show_hide_btn = $root.find("[data-pass-show-hide]");
    const pass_show = $root.find("[data-pass-show]");
    const pass_hide = $root.find("[data-pass-hide]");
    $(pass_hide).hide();
    $(pass_show_hide_btn).click(function () {
      if (pass_elemet.attr("type") === "password") {
        pass_elemet.attr("type", "text");
        $(pass_show).hide();
        $(pass_hide).show();
      } else {
        pass_elemet.attr("type", "password");
        $(pass_hide).hide();
        $(pass_show).show();
      }
    });
  }
  $.fn.Pass_Show_Hide = jQueryPlugin("Pass_Show_Hide", Pass_Show_Hide);
  $("[data-password]").Pass_Show_Hide();
})();
 """,},
    
    {"html": """<body>
  
  <div>
    
    <input type="text" id="form" placeholder="Example">
      
      <input type="submit" id="button" value="Enter"> """,
     "css": """body {
  background: linear-gradient(to left top, #22132e, #000) fixed;
}

div {
  margin: auto;
  position:relative;
  top: 200px;
  width: 40%;
}

#form {
  width: 400px;
  padding: 10px;
  font-size: 18px;
  outline:none;
  background: linear-gradient(to left top, #000, #22132e) fixed;
  border-radius: 10px;
  border: 2px solid rgba(255,255,255,0.2);
  color: rgba(255,255,255,0.8);
  transition: all 0.5s;
}

#form:hover {
  border: 2px solid rgba(255,255,255,0.5);
}
#form:focus {
  border: 2px solid rgba(255,255,255,0.5);
  background: linear-gradient(to left top, #000, #4e2d69) fixed;
}

#button {
  width: 425px;
  padding: 10px;
  margin-top: 10px;
  font-size: 15px;
  font-weight:bold;
  outline:none;
  background: linear-gradient(to left top, #000, #4e2d69) fixed;
  border-radius: 10px;
  border: 5px solid rgba(255,255,255,0.2);
  color: rgba(255,255,255,0.8);
  transition: all 0.5s;
}

#button:hover {
  border: 5px solid rgba(255,255,255,0.5);
  background: linear-gradient(to left top, #000, #8b5db0) fixed;
}

#button:focus {
  background: linear-gradient(to left top, #8b5db0, #000) fixed;
} """,
     "js": """ """,},
    
    {"html": """<form action="">
  <div class="inp-border a1">
      <input class="input" type="text" name="name1" placeholder="Your Name">
  </div>
  <div class="inp-border a2">
      <input class="input" type="text" name="name1" placeholder="Your Name">
  </div>
  <div class="inp-border a3">
      <input class="input" type="text" name="name1" placeholder="Your Name">
  </div>
  <div class="inp-border a4">
      <input class="input" type="text" name="name1" placeholder="Your Name">
  </div>
</form>
 """,
     "css": """ body{
  margin: 0;
  padding: 0;
  background: #252525;
  position: absolute;
  top: 50%;
  left:50%;
  transform: translate(-50%, -50%);
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
/* by Ruben Vardanyan */
.inp-border{
	padding: 5px;

	margin: 2vh 1vh;
	border-radius: 67px;
  max-width:200px;
  
}
input{
	font-size: 17px;
}
.input{
  text-align:center;
	padding: 15px;
	outline: none;
	border:double 0;
	background: #252525;
	border-radius: 67px;
	position: relative;
	box-sizing: border-box;
	display: block;
  width: 100%;
}
.a1{
  background: linear-gradient(330.28deg,#FF6E1D  100%,#FF6E1D  100%,#FF6E1D  100%);
  
}
.a1 >input{
  color: #FF6E1D;
}
.a1 >input::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #FF6E1D;
  opacity: 0.6; /* Firefox */
}
.a2{
   background: linear-gradient(330.28deg,#2CFFF2  100%,#2CFFF2  100%,#2CFFF2  100%);
}
.a2 >input{
  color: #2CFFF2;
}
.a2 >input::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #2CFFF2;
  opacity: 0.6; /* Firefox */
}
.a3{
  background: linear-gradient(330.28deg,#FF54A6  100%,#FF54A6  100%,#FF54A6  100%);
}
.a3 >input{
  color: #FF54A6;
}
.a3 >input::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #FF54A6;
  opacity: 0.6; /* Firefox */
}
.a4{
  	background: linear-gradient(330.28deg,#FF3E3E  100%,#FF3E3E  100%,#FF3E3E  100%);
}
.a4 > input{
 color:#FF3E3E;
}
.a4 >input::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #FF3E3E;
  opacity: 0.6; /* Firefox */
}
.inp-border:focus-within{

		background: linear-gradient(330.28deg,#2CFFF2       0%, #1E78FF  30.73%, #FF54A6  55.73%, #FF6E1D       79.17%, #FF3E3E  100%);
}
.inp-border:hover{
		background: linear-gradient(330.28deg,#2CFFF2       0%, #1E78FF  30.73%, #FF54A6  55.73%, #FF6E1D       79.17%, #FF3E3E  100%);
}""",
     "js": """ """,},
    
    {"html": """ <section class="data-search">
  <form method="post">
    <div class="form-group">
      <div class="head">
        <div class="svg">
          <svg id="b68b2dea-431f-4b15-9350-961d32a371b9" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="200" height="200.96158" viewBox="0 0 888 637.96158"><title>adventure</title><circle cx="174.02316" cy="76.13114" r="30.99674" fill="#2f2e41"/><path d="M235.61478,580.54458l19.04375-66.04535,6.483,2.02593s-7.69854,49.43272-19.85412,61.99349Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><path d="M308.14311,226.00667s2.43112,25.93191-3.24149,33.22527,3.64667,21.47486,3.64667,21.47486l17.01782,20.25931,25.12155-11.34521,3.64667-21.06968-2.43111-14.58671s-8.50891-8.50891-4.86224-23.906S308.14311,226.00667,308.14311,226.00667Z" transform="translate(-156 -131.23696)" fill="#ffb9b9"/><path d="M308.14311,226.00667s2.43112,25.93191-3.24149,33.22527,3.64667,21.47486,3.64667,21.47486l17.01782,20.25931,25.12155-11.34521,3.64667-21.06968-2.43111-14.58671s-8.50891-8.50891-4.86224-23.906S308.14311,226.00667,308.14311,226.00667Z" transform="translate(-156 -131.23696)" opacity="0.1"/><polygon points="166.73 579.778 166.73 596.39 189.015 600.847 186.989 573.295 166.73 579.778" fill="#ffb9b9"/><polygon points="233.586 573.295 228.723 596.39 238.448 603.278 255.466 590.718 253.44 570.863 233.586 573.295" fill="#ffb9b9"/><path d="M347.041,730.05829s-8.50891-14.38252-24.31117-5.36792c0,0-2.8363,15.90276-5.67261,17.11832s-18.63856,24.31117,0,26.3371,27.95785-4.05186,27.95785-4.05186-3.64667,3.13776,2.02593,1.517,3.24149-10.53484,3.24149-10.53484Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><path d="M402.55149,720.33382s-12.56077,8.91409-14.5867,4.86223-5.26742-3.64667-5.26742-3.64667-11.34522,42.76822-4.05186,44.79415A24.58356,24.58356,0,0,0,392.827,765.611s9.72447-6.81038,9.72447-1.543,27.14748,4.88816,38.49269,4.483,5.26742-8.91409,5.26742-8.91409l-14.99189-14.5867-17.01782-24.71636S406.60335,713.44565,402.55149,720.33382Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><path d="M283.02156,449.26426l17.01782,163.29s9.31929,99.6758,10.94,101.29655,12.15559,6.88816,35.2512,0l-5.26742-130.46995,9.72447-81.03724,22.28524,55.91569s5.26742,150.32408,8.91409,150.32408,25.93192,7.29335,31.19934-1.62075,4.45705-104.94322,4.45705-104.94322-2.43112-151.53963-20.25931-156.40187S283.02156,449.26426,283.02156,449.26426Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><circle cx="174.02316" cy="81.80375" r="27.95785" fill="#ffb9b9"/><path d="M331.64391,290.83646s-2.83631-17.423-2.83631-20.6645-12.56077-5.26742-12.56077-5.26742-9.72447-10.94-11.7504-9.31928-32.82008,22.28524-37.68231,25.12154-10.12966,14.99189-9.72447,15.80226,25.52673,53.48458,25.52673,53.48458,10.94,32.4149,3.24149,49.43272-17.423,50.64827-3.24149,57.53644,83.06317,21.88,95.62394,8.91409,21.47487-16.61263,24.71636-16.61263-13.37115-56.32088-9.72447-61.5883-1.62075-38.0875-1.62075-38.0875l18.63857-52.269s-1.62075-29.17341-38.49269-35.65639L349.699,250.968Z" transform="translate(-156 -131.23696)" fill="#575a89"/><path d="M255.87409,456.55761s-2.02593,19.44894-2.02593,25.12154-9.72447,38.89788,4.457,42.94974,12.966-44.1653,12.966-44.1653V455.74724Z" transform="translate(-156 -131.23696)" fill="#ffb9b9"/><path d="M424.02636,438.32423s2.43112,18.63857,1.21556,22.69043,11.7504,39.30306-5.67261,41.329-12.966-42.13937-12.966-42.13937v-21.88Z" transform="translate(-156 -131.23696)" fill="#ffb9b9"/><path d="M252.22741,574.0616l11.7504-62.39867h3.64668a24.5429,24.5429,0,0,1,3.64668,23.5008c-4.86224,13.77633-8.9141,38.89787-8.9141,38.89787Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><path d="M263.16744,291.64683l-6.07779,4.86223s-8.10372,128.84921-6.07779,138.57368-7.29336,23.5008.81037,24.71636,17.82819,6.483,22.28524,3.24149,5.26742-14.99189,6.88816-17.82819,4.457-36.46676,4.457-36.46676,8.50891-33.63045,3.24149-58.752-10.12965-50.64827-10.12965-50.64827Z" transform="translate(-156 -131.23696)" fill="#575a89"/><path d="M391.61146,281.51718,410.25,297.31944l14.18151,82.658s8.9141,64.4246,2.02594,65.235-17.423-1.21556-21.88006,0-8.10372-2.02594-8.10372-2.02594-4.86224-25.93191-4.86224-26.3371S388.37,386.86558,388.37,386.86558l-4.05186-33.22526,6.07779-36.46676Z" transform="translate(-156 -131.23696)" fill="#575a89"/><path d="M303.68606,664.01294s-2.63371,7.56482-6.26416,17.86464c-1.68559,4.78931-3.58594,10.17425-5.543,15.66451-1.26012,3.54944-2.54048,7.14344-3.80065,10.65234-2.00971,5.61184-3.96273,11.00082-5.66855,15.628-2.25286,6.10616-4.08025,10.89141-5.06077,13.124-4.457,10.12966-85.89947-6.07779-92.38245-10.12965s-8.10373-17.8282-8.9141-37.27713c-.00405-.1013-.00811-.2026-.00811-.30389-.10535-3.92626.89545-9.77309,2.56892-16.63289.83465-3.42788,1.83951-7.107,2.95783-10.92788,1.49921-5.12562,3.201-10.49837,4.9797-15.84683,7.64185-22.97406,16.64914-45.42947,16.64914-45.42947s15.80226-10.94,21.47486-18.23338,36.872-12.966,36.872-12.966c8.91409.40519,29.1734,34.846,37.27713,45.38085S303.68606,664.01294,303.68606,664.01294Z" transform="translate(-156 -131.23696)" fill="#3f3d56"/><circle cx="102.30521" cy="467.541" r="3.64668" fill="#2f2e41"/><circle cx="107.97781" cy="471.59286" r="2.02593" fill="#2f2e41"/><path d="M297.4219,681.87758c-1.68559,4.78931-3.58594,10.17425-5.543,15.66451L181.57105,661.675c1.49921-5.12562,3.201-10.49837,4.9797-15.84683Z" transform="translate(-156 -131.23696)" fill="#f2f2f2"/><path d="M288.07828,708.19443c-2.00971,5.61184-3.96273,11.00082-5.66855,15.628L176.0443,689.23578c-.10535-3.92626.89545-9.77309,2.56892-16.63289Z" transform="translate(-156 -131.23696)" fill="#f2f2f2"/><path d="M258.30521,599.58833s8.10372,35.65639,3.24149,67.26091,12.15558,61.18312,12.15558,61.18312" transform="translate(-156 -131.23696)" fill="none" stroke="#2f2e41" stroke-miterlimit="10" stroke-width="3"/><path d="M263.97781,602.42464s-15.80226,57.53644-16.20744,65.64016-6.88817,66.04535-14.99189,72.12314" transform="translate(-156 -131.23696)" fill="none" stroke="#2f2e41" stroke-miterlimit="10" stroke-width="3"/><path d="M308.55947,195.98021s-6.32846-16.454,2.84781-21.83318l2.53138,7.27773s23.09887-13.92261,29.1109-10.75838l-5.69561,7.59415s26.89594,0,28.79448,10.442l-9.49269.31642s10.12554,6.64488,10.442,17.40326l-20.25106,1.26569,9.8091,5.69561s-36.705,5.06276-45.56489-9.49269Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><path d="M303.07828,196.63067s7.29335,14.5867,17.01782,10.94,0-17.01782,0-17.01782l-6.483-3.24149Z" transform="translate(-156 -131.23696)" fill="#2f2e41"/><path d="M932,426.75091,799.74956,261.48738A44.40268,44.40268,0,0,1,778.3615,272.287c-24.89751,4.90336-49.21219-12.0988-54.30837-37.97538a47.96607,47.96607,0,0,1,16.55848-46.72451L695.518,131.237,438.61481,350.80025l236.482,295.514Z" transform="translate(-156 -131.23696)" fill="#f2f2f2"/><circle cx="611.6739" cy="95.91464" r="37.28363" fill="#f2f2f2"/><rect x="539.17344" y="391.09034" width="17.448" height="50.7929" transform="translate(-281.46197 427.51701) rotate(-49.17044)" fill="#4ecca3"/><rect x="784.05171" y="628.18934" width="17.448" height="45.02318" transform="translate(-373.90779 693.8884) rotate(-49.17044)" fill="#4ecca3"/><path d="M843,531.04734V532.071q-.03493,3.85593-.221,7.67709a170.99032,170.99032,0,0,1-341.41084,2.23332q-.349-5.42629-.349-10.934a170.14342,170.14342,0,0,1,31.44133-98.83715q2.46012-3.4896,5.118-6.85119c1.22134-1.55872,2.47762-3.08251,3.74554-4.59465a171.02253,171.02253,0,0,1,238.29313-22.61261c2.05889,1.66336,4.08285,3.38488,6.06023,5.14132q2.373,2.11125,4.66444,4.3155A170.52787,170.52787,0,0,1,842.40676,516.6702Q843,523.78892,843,531.04734Z" transform="translate(-156 -131.23696)" fill="#3f3d56"/><path d="M672.0096,723.55694c-106.14995,0-192.5096-86.35965-192.5096-192.5096a191.88044,191.88044,0,0,1,51.366-130.9151l4.26317,3.95647A186.0788,186.0788,0,0,0,485.316,531.04734c0,102.9432,83.7504,186.6936,186.6936,186.6936a185.217,185.217,0,0,0,134.02586-56.72532l4.1757,4.04849A190.98693,190.98693,0,0,1,672.0096,723.55694Z" transform="translate(-156 -131.23696)" fill="#4ecca3"/><rect x="495.072" y="588.24878" width="48.8544" height="48.8544" fill="#4ecca3"/><path d="M537.57858,425.359a.95129.95129,0,0,1,.23264.13959c.91892.75608-.23264,2.21008-.09306,3.40817.16285,1.53543,2.21008,1.87276,3.75714,2.024,1.54705.16285,3.50123,1.40747,2.76841,2.78005-3.88509,1.33768-7.8167.02326-11.78321-1.50053a170.1436,170.1436,0,0,0-31.4413,98.83711q0,5.51356.349,10.93408a4.41991,4.41991,0,0,0,1.05851.57c1.1632.442,2.51251.3606,3.58266.98872.84913.50018,1.4191,1.38421,2.26824,1.84949,2.43109,1.32605,5.80437-1.22136,8.07261.36059a20.85731,20.85731,0,0,1,1.66337,1.69828c2.09376,1.81459,5.53683.59323,7.95629,1.95417,1.55869.8724,2.3613,2.6172,3.1988,4.19915,2.08213,3.95488,5.45541,7.84,9.91046,8.154a26.68761,26.68761,0,0,1,4.21079.13958c1.37257.31406,2.72189,1.51216,2.50088,2.89637-.38386,2.38456.791,4.99013.47691,7.37469-.57,4.362-6.74656,6.26964-7.27,10.63164a26.26422,26.26422,0,0,1-.16285,2.87311c-.27917,1.13993-1.13993,2.07049-1.44237,3.21043-.5816,2.15192.96546,4.30384,2.6521,5.74621,1.69827,1.454,3.72224,2.71025,4.6528,4.73422.97709,2.15192.50018,4.6528.81424,6.99083.69792,5.10645,5.10645,8.88685,9.64293,11.32957a10.06848,10.06848,0,0,1,3.76877,2.74515c1.1632,1.68664,1.04688,3.90836,1.44236,5.92069.95383,4.92034,5.09482,8.97991,5.21114,13.9933.08142,3.571-1.896,6.80472-3.08248,10.16637a23.46244,23.46244,0,0,0-1.05851,10.9806,171.80947,171.80947,0,0,0,21.08881,15.29608,6.14415,6.14415,0,0,0,.8724-1.95417,3.86492,3.86492,0,0,0-1.803-4.00141,9.56227,9.56227,0,0,0,3.33839-2.14029,3.27477,3.27477,0,0,0,.60486-3.699c2.04723.2559,4.47832.38385,5.82763-1.18647,1.08178-1.25625,1.012-3.14064.5816-4.73422a19.52515,19.52515,0,0,1-1.1632-4.81565,86.62334,86.62334,0,0,0,14.21431-.47691,9.22747,9.22747,0,0,0-4.32711-5.42051c2.14029-.3606,4.08284-2.91964,4.75749-4.9785a12.68072,12.68072,0,0,0,.09306-6.4325,3.42171,3.42171,0,0,1-.06979-1.675,3.29552,3.29552,0,0,1,1.69827-1.64012q5.30419-3.0534,10.60838-6.09516a6.396,6.396,0,0,0,1.69827-1.24463c1.105-1.31441.9422-3.28022.37223-4.89707s-1.47727-3.14064-1.69827-4.83891c-.6514-5.08319,4.79238-8.73563,6.63024-13.528a20.31775,20.31775,0,0,0,1.00035-5.92069c.15121-2.16355.16285-4.66443-1.4889-6.04864-1.59358-1.33768-4.0712-1.03524-5.73457-2.27987-1.5238-1.13993-2.04724-3.33838-3.71061-4.25731-1.51216-.8375-3.39655-.30243-5.08319-.69792-2.95452-.68629-4.81564-4.09446-7.84-4.40853-1.69828-.18611-3.62919.65139-5.025-.33733-1.233-.884-1.27952-2.64046-1.51216-4.12936a11.53517,11.53517,0,0,0-9.3056-9.32886c-1.75643-.27917-3.66408-.17448-5.16461-1.13994-1.51216-.97708-2.19844-2.80331-3.39654-4.16425-1.90765-2.17519-4.932-2.95453-7.75854-3.61755q-5.75784-1.3435-11.504-2.69863c-2.0356-.48854-4.66443-.74445-5.76947,1.04688a7.86927,7.86927,0,0,0-.67466,2.15192,6.67341,6.67341,0,0,1-6.258,4.69933,7.39431,7.39431,0,0,0-4.35036-3.37328,27.44775,27.44775,0,0,1-3.53613-.8375,4.95427,4.95427,0,0,1-2.14029-6.87452,6.17223,6.17223,0,0,0-1.05851-7.40958c-1.95418-1.75643-4.78075-2.18682-7.40959-2.01234-.68628-1.50052.46528-3.18716,1.69828-4.28057,1.24462-1.08178,2.74515-2.15192,3.01268-3.7804.43039-2.559-2.8382-4.50159-5.31582-3.74551-2.47762.76772-4.05957,3.17554-5.10645,5.54847a16.73353,16.73353,0,0,1-2.05886,3.94325,4.042,4.042,0,0,1-3.90835,1.60521c-2.04724-.52344-2.82658-2.95453-3.28023-5.00176a32.61424,32.61424,0,0,1-1.09341-8.38667,10.948,10.948,0,0,1,3.16391-7.63059c3.38491-3.11738,8.596-2.815,13.16742-2.31477a3.35392,3.35392,0,0,1,.349-4.42016,5.02569,5.02569,0,0,1,4.55975-1.11667,6.256,6.256,0,0,1,3.52449,2.10539c1.30279,1.582,1.675,3.73387,2.6521,5.5252.98872,1.803,3.1988,3.33838,5.00176,2.37293,1.57032-.83751,1.81459-3.00106,1.43073-4.73423-.39548-1.72153-1.22136-3.40817-1.08177-5.17624.26753-3.36164,3.76877-5.39724,6.85125-6.78145s6.607-3.257,7.09552-6.607a6.17389,6.17389,0,0,1,.37222-1.90765,3.72933,3.72933,0,0,1,1.38421-1.30278c8.99153-5.944,18.14592-11.96933,28.42861-15.21466.53507-.17448.59323.01164,1.13993-.11632.76771-.442.25591-1.66337-.47691-2.15192s-1.7099-.8724-1.896-1.73316c-.128-.62813.24428-1.25626.33733-1.896a2.36721,2.36721,0,0,0-3.10574-2.39619c-.82587-1.09341.80261-2.3613,2.12865-2.73352a58.13863,58.13863,0,0,1,12.15544-1.97744,2.16447,2.16447,0,0,1,1.38421.23264,1.645,1.645,0,0,1,.10469,2.25661,12.73993,12.73993,0,0,1-1.84949,1.68664,5.08082,5.08082,0,0,0-1.32605,5.10644c2.15192,1.09341,4.47832,2.22172,6.86288,1.83786,2.37293-.38386,4.47832-3.05922,3.36165-5.18787-1.03525-1.98907-4.16425-2.44272-4.69933-4.61791-.62812-2.5474,2.9778-4.81564,2.16356-7.30489-.349-1.09341-1.44237-1.7448-2.27988-2.52415a6.882,6.882,0,0,1-1.50052-7.60732,8.66758,8.66758,0,0,1-7.58407-2.37293c-1.81459-1.82623-3.257-4.72259-5.83926-4.62954-2.3613.06979-4.3969,2.82658-6.607,1.98907-.5467-.20937-1.11667-.62812-1.64011-.38385a1.35575,1.35575,0,0,0-.6165,1.012c-.55833,2.687.40712,5.74621-1.05851,8.07261-1.59358,2.52414-5.28093,2.8731-7.21184,5.153-1.04688,1.233-1.454,2.89636-2.41945,4.19915s-3.00106,2.14029-4.16426,1.00035a5.73208,5.73208,0,0,0-1.55869-6.9792,14.98861,14.98861,0,0,0-3.44307-1.675,20.43352,20.43352,0,0,1-3.85019-2.14029,3.81527,3.81527,0,0,1-1.40747-1.51216,3.47684,3.47684,0,0,1,.093-2.39619,9.79355,9.79355,0,0,1,7.78181-6.44413c1.53542-.20937,3.32675-.13958,4.35037-1.31441.53507-.6165.81424-1.55869,1.60521-1.803a2.34021,2.34021,0,0,1,1.47727.17448c1.91928.67465,3.82693,1.34931,5.74621,2.024a3.93612,3.93612,0,0,0,2.04723.33732,1.37705,1.37705,0,0,0,1.19809-1.454c-.18611-.95382-1.65174-1.40747-1.51216-2.37292a1.50855,1.50855,0,0,1,.47692-.81424,20.55375,20.55375,0,0,1,16.29643-6.4325c.72118,1.1981-.41875,2.60557-1.38421,3.61755-.95382,1.02362-1.72154,2.83821-.55834,3.61755a3.06427,3.06427,0,0,0,1.5238.349,13.29118,13.29118,0,0,1,4.0712,1.233c1.98907.86076,3.94324,1.81459,5.85089,2.8382a7.37635,7.37635,0,0,1,.13959-3.76876,2.55938,2.55938,0,0,1,3.02432-1.64012c1.13993.442,1.72153,1.95418,2.94289,2.09376,1.61685.18612,2.25661-2.21008,1.582-3.699s-2.024-2.72189-2.12865-4.362c-.08143-1.09341.33733-2.45435-.53507-3.11738a2.31414,2.31414,0,0,0-1.03525-.37222q-10.95735-2.00652-21.92632-4.02467c-1.30279-.24428-3.17554-.05816-3.2337,1.25625-.03489.74445.62813,1.47727.33733,2.15192-.31406.72119-1.33768.663-2.08213.91893a2.827,2.827,0,0,0-1.62848,2.98942,8.14854,8.14854,0,0,0,1.37258,3.36165c-1.43074-.59323-3.58266-.69792-5.01339-1.30278a19.296,19.296,0,0,0-1.25626-4.82728,1.70385,1.70385,0,0,0-2.22171-1.37258c-1.88439.2908-3.76877.57-5.65315.86077a2.18661,2.18661,0,0,0-1.29116.50018c-.73281.77934-.01163,2.024-.03489,3.09411a2.89958,2.89958,0,0,1-2.245,2.50088,8.46226,8.46226,0,0,1-3.58265-.04653c-2.64047-.40712-5.2693-.81424-7.90976-1.22136a12.95718,12.95718,0,0,0,5.97884-4.00141c1.04688-1.233,1.60522-3.53613.09306-4.11773a3.60875,3.60875,0,0,0-1.37258-.10468c-3.58265.02326-6.40923-2.96616-9.75924-4.234a9.59326,9.59326,0,0,0-3.29186-.60487Z" transform="translate(-156 -131.23696)" fill="#4ecca3" class="pat1"/><path d="M842.779,539.74807a4.20005,4.20005,0,0,1-3.55939,1.68664c-3.64082-.31406-5.17624-5.56009-8.78216-6.15333a1.40537,1.40537,0,0,0-.95382.09306c-.53508.2908-.62813,1.012-.663,1.61685-.15121,3.001-.27917,6.11843.89567,8.88685,1.7099,4.04793,6.14169,7.44448,5.21113,11.73668-5.00176-2.31476-7.60733-7.933-8.78216-13.31864-1.18646-5.38561-1.37257-11.03876-3.4896-16.13358-1.61685,2.05886-4.99013.36059-6.45576-1.803-1.39584-2.04723-2.25661-4.42016-3.60592-6.50229-1.34931-2.07049-3.41981-3.93161-5.88579-4.04793-2.59394-.11632-4.85054,1.66337-6.828,3.35a15.80206,15.80206,0,0,0-4.24568,4.72259c-1.38421,2.79168-1.02362,6.07191-1.09341,9.17765-.06979,3.35-.77935,6.89778-3.07085,9.36376-2.2915,2.45435-6.51392,3.31512-9.03806,1.09341a10.1961,10.1961,0,0,1-2.52415-4.54811,221.31754,221.31754,0,0,1-6.83961-24.40394c-.41876,1.88439-2.08213,4.31547-3.66408,3.21043a3.26712,3.26712,0,0,1-.83751-1.0934c-2.95453-4.99013-8.40993-7.99119-13.93513-9.79415-5.51357-1.79133-11.31794-2.62883-16.77335-4.60627a42.88523,42.88523,0,0,1-8.71237-4.33874,6.86049,6.86049,0,0,0-.41875,7.00247,5.60935,5.60935,0,0,0,6.30455,2.64046c1.20972-.39549,2.23334-1.233,3.43144-1.65174,1.19809-.40712,2.81494-.20938,3.33838.95382.51181,1.105-.2559,2.44272.12795,3.60592.57,1.75643,3.2337,1.896,4.16426,3.50123a3.241,3.241,0,0,1-.8724,3.74551,15.67623,15.67623,0,0,1-3.51287,2.16355c-3.90835,2.17518-6.6884,5.88579-10.1082,8.77053-3.41981,2.89637-8.24709,5.00176-12.31829,3.15227.96545-4.92034-4.88544-8.52626-5.96722-13.42333-.36059-1.61685-.17448-3.32675-.67465-4.89707-.73282-2.27987-2.75679-3.83856-4.40853-5.5601a21.85517,21.85517,0,0,1-5.99048-15.87768c.093-2.024.46528-4.08283,0-6.06027-.45365-1.96581-2.09376-3.87345-4.11773-3.792-4.6179.20938-10.44554.55834-12.865-3.38491-.8724-1.40747-1.24463-3.46634.01163-4.54811a4.39171,4.39171,0,0,1,3.33838-.57c3.478.33733,6.94431.68629,10.42228,1.02361,2.43108.23264,5.05992.43039,7.15368-.8375s3.001-4.6528,1.05851-6.15333c-1.40747-1.09341-3.94325-1.03525-4.362-2.76841-.33733-1.454,1.26789-3.09412.39549-4.31548-.6165-.86076-2.01234-.62812-2.86148.02327a18.69439,18.69439,0,0,1-2.40782,2.10539c-1.66338.86077-3.64082.0349-5.43214-.52344s-4.18752-.60486-5.04829,1.05851c-.97709,1.84949.84913,4.29221-.10469,6.15333-1.27952,2.45435-5.58336,1.05851-7.37469,3.17554-2.04723,2.41945,1.39584,6.04864.70955,9.14275a5.69965,5.69965,0,0,1-5.61825-.31407,5.439,5.439,0,0,1-2.34967-5.07155c.16285-1.39584.89567-2.82657.40712-4.141a4.83418,4.83418,0,0,0-2.45435-2.245q-5.05992-2.80912-10.11984-5.595c-.94219,1.7448.24427,3.89672,1.73317,5.21114,1.47726,1.30278,3.33838,2.2915,4.31547,4.013a5.27443,5.27443,0,0,1-1.97744,6.95593,1.227,1.227,0,0,1-1.012.17448,1.40226,1.40226,0,0,1-.65139-.8724c-1.7797-4.57137-4.46669-9.073-8.74727-11.45752-4.29221-2.39619-10.44553-1.896-13.26048,2.117-.663.95382-1.11667,2.04723-1.69827,3.05921-3.08248,5.36236-9.71272,7.89813-15.90094,7.73528a3.06444,3.06444,0,0,1-1.73317-.40712c-1.00035-.68628-.95383-2.15192-.80261-3.36164.221-1.70991.43038-3.40818.65139-5.11808a4.099,4.099,0,0,1,1.12831-2.80332c1.15156-.90729,2.80331-.33732,4.26894-.36059a5.37747,5.37747,0,0,0,4.89707-3.7804,6.07682,6.07682,0,0,0-1.69827-6.04864c-.663-.62813-1.55869-1.4191-1.20973-2.26824a1.885,1.885,0,0,1,1.31442-.884c2.6172-.75608,5.39725-.95382,7.96792-1.86112,2.5823-.89566,5.08318-2.73352,5.69968-5.39725.18611-.81424.26753-1.803,1.00035-2.21008a3.23975,3.23975,0,0,1,1.1632-.23264,5.66134,5.66134,0,0,0,4.85054-5.89742c1.233-.86077,2.96616-.221,4.16426.69792,1.18646.91893,2.245,2.12865,3.699,2.52414,2.71025.74445,5.32745-1.66337,8.1424-1.675,1.18646,0,2.40782.41876,3.51286.01164,1.1283-.40712,1.803-1.5238,2.66373-2.34967.8724-.8375,2.38456-1.33768,3.18717-.442-.23264-1.68664-.45365-3.36165-.68629-5.03666a9.90135,9.90135,0,0,0,8.061-1.46563c-2.93126-.98872-5.85089-1.97744-8.78216-2.96616a1.89514,1.89514,0,0,1-.82587-.442c-.63976-.68629,0-1.75643.51181-2.53577,1.24462-1.87276,1.454-4.95524-.59323-5.8858-1.39584-.63976-2.98943.128-4.32711.8724-2.14028,1.18647-4.28057,2.38456-6.42086,3.571-.19774,1.22136,1.29115,1.91928,2.21008,2.73352a3.70647,3.70647,0,0,1-2.41946,6.479,4.64331,4.64331,0,0,1,.82588,3.92c-1.43074.10468-2.87311.20937-4.31548.31406a1.85325,1.85325,0,0,1-1.39584-.27917c-.46528-.40712-.39548-1.1283-.5118-1.73317a3.74393,3.74393,0,0,0-3.16391-2.75678,10.9223,10.9223,0,0,0-4.40853.40712,2.68616,2.68616,0,0,1-1.90764-.04653,1.903,1.903,0,0,1-.74445-.95382,4.86365,4.86365,0,0,1,.97709-4.67607,26.76673,26.76673,0,0,1,3.67571-3.38491,21.428,21.428,0,0,0,6.386-9.8872c2.37292-1.00035,4.82728-2.34966,7.21184-3.35a28.80944,28.80944,0,0,1,5.99048-2.01234,28.30911,28.30911,0,0,1,5.87416-.27917c2.67536.04653,5.36235.09306,8.03771.15122a19.34408,19.34408,0,0,1,7.03736,1.012c2.19845.9073,4.141,2.87311,4.29221,5.246a1.61075,1.61075,0,0,1-.52344,1.47727,1.885,1.885,0,0,1-1.012.23264c-2.22171.06979-3.1639.62813-5.38561.70955,1.40747,1.50053,2.98942,3.08248,5.03665,3.35,3.60592.46528,6.19986-3.2686,7.86323-6.51392a3.17423,3.17423,0,0,0,3.31512,2.94289,6.685,6.685,0,0,0,2.50088-.97709,49.19541,49.19541,0,0,1,23.32216-6.02537,2.51131,2.51131,0,0,1,1.91928-2.76842c1.66338-.32569,3.15228,1.105,3.95488,2.59394.791,1.48889,1.29116,3.21043,2.57068,4.3271,1.26788,1.11667,3.72224,1.05851,4.22241-.5467.48855-1.54706-1.1283-2.87311-2.466-3.792-1.34931-.9073-2.75679-2.59394-1.84949-3.94325,6.83962-1.52379,13.73739-3.036,20.75149-3.33839a8.83055,8.83055,0,0,0,3.4896-.60486,2.71244,2.71244,0,0,0,1.62848-2.8731,7.93083,7.93083,0,0,1-8.25872-3.11738c7.20021-.59323,14.73774-1.11667,21.65878.50018l6.06027,5.14134c-1.15156,1.1981-2.687,2.3264-1.84948,3.5245a2.5785,2.5785,0,0,0,2.12865.73281c1.46563.02327,2.93127.05816,4.38527.05816a170.52828,170.52828,0,0,1,52.06483,109.06163c-2.44272-.093-4.6877,3.00106-4.37363,5.69968.37222,3.129,2.62883,5.64152,4.24568,8.34015A12.70881,12.70881,0,0,1,843,532.071Z" transform="translate(-156 -131.23696)" fill="#4ecca3" class="pat2"/><line y1="636.96158" x2="888" y2="636.96158" fill="none" stroke="#3f3d56" stroke-miterlimit="10" stroke-width="2"/><circle cx="366.35223" cy="65.26967" r="14.75556" fill="none" stroke="#3f3d56" stroke-miterlimit="10" stroke-width="2"/><circle cx="802.35223" cy="346.26967" r="14.75556" fill="none" stroke="#3f3d56" stroke-miterlimit="10" stroke-width="2"/><circle cx="701.61889" cy="199.26967" r="14.75556" fill="none" stroke="#3f3d56" stroke-miterlimit="10" stroke-width="2"/><circle cx="604.80775" cy="323.9214" r="16.55902" fill="#3f3d56"/><circle cx="657.99881" cy="270.69736" r="21.82779" fill="#fff"/><path d="M836.0738,379.30567a30.86,30.86,0,0,0-43.63926.54048c-11.9014,12.1999-28.89284,73.81079-28.89284,73.81079s61.17118-18.51211,73.07258-30.712A30.86,30.86,0,0,0,836.0738,379.30567Zm-32.06129,32.86542a14.301,14.301,0,1,1,20.22307-.25047A14.301,14.301,0,0,1,804.01251,412.17109Z" transform="translate(-156 -131.23696)" fill="#57b894"/></svg>
          
        </div>
      
      <div class="title">
        <h1 class="text"> 
          Find Your   
        </h1>
        <div class="brand">
          <h1>
          <span>H</span>
          <span>o</span>
          <span>t</span>
          <span>e</span>
          <span>l</span>
          </h1>
        </div>
      </div>
      </div>
      <div class="input-group">
        <input type="text" class="form-control" placeholder="Type to Search">
        <select class="form-control">
          <option>select</option>
          <option>params 1</option>
          <option>params 2</option>
          <option>params 3</option>
        </select>
        <button type="button" class="btn">Search</button>
      </div>
    </div>
  </form>
</section>""",
     "css": """@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&family=Roboto:wght@400;500;700&display=swap');
*{
  padding: 0;
  margin: 0;
  box-sizing:border-box;
}
.data-search{
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #232931;
  font-family: "roboto", cursive;
}

.input-group{
  display: flex;
  border-radius:7px;
  overflow: hidden;
}

.form-control, .btn{
  height:40px;
  border: none;
  outline:none;
  font-size: 1em;
  font-weight: 500;
  padding: 0 7px;
  background: #393e46;
  transition: .3s ease;
  color: #4ecca3;
}

input.form-control{
  width: 350px;
}

.btn{
  background-color: #4ecca3;
  color:#232931;
  cursor:pointer;
}

select:hover{
  box-shadow: inset 0 0 100px rgba(0,0,0,.2);
}

.btn:hover{
  box-shadow: inset 0 0 100px rgba(255,255,255,.2);
}

.form-control:focus{
  box-shadow: inset 0 0 100px rgba(0,0,0,.2);
}
.pat1{
  animation:changeColorPath1 1.5s linear infinite;
}
.pat2{
  animation:changeColorPath2 1.5s linear infinite;
}
.form-control::placeholder{
  color: #4ecca3;
}

.title .text{
  font-size: 3em;
  animation:changeColor 1.5s linear infinite;
}
.title .brand h1{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 10px;
}
.title{
  text-align: center;
  margin: -20px 0 10px 0;
  display: flex;
  justify-content: center;
}

.title .brand h1{
  font-size: 3em;
  color:#393e46;
}
.title .brand h1 span{
  transition: .15s ease;
}
.title .brand h1 span:hover{
  color: #4ecca3;
}

.head{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction:column;
}
select:focus{
  
}
.head .svg{
  width: 200px;
  overflow:hidden;
}

.head .svg svg{
  width: 100%;
  animation: popUp 1s linear;
}

@keyframes popUp {
  0%{
    transform: translateY(150px);
    opacity: 0;
  }
  100%{
    transform: translateY(0);             opacity: 1;
  }
}
@keyframes changeColor{
  0% {
    color:#393e46;
  }
  50% {
    color:#4ecca3;
  }
  100% {
    color:#393e46;
  }
}
@keyframes changeColorPath1{
  0% {
    fill:#393e46;
  }
  50% {
    fill:#c61951;
  }
  100% {
    fill:#393e46;
  }
}@keyframes changeColorPath2{
  0% {
    fill:#393e46;
  }
  50% {
    fill:#4ecca3;
  }
  100% {
    fill:#393e46;
  }
} """,
     "js": """ """,},
    
    {"html": """<div class="demo">
  <form class="form" action="submit">
    <label for="name">Subscribe Today!</label>
    <input class="form__inset" type="text" placeholder="Email" name="email">
  </form>
</div> """,
     "css": """// Variables
$color-background: hsl(224, 24%, 32%);
$color-inset: hsl(230, 22%, 27%);
$shadow-inset: inset 0 2px 2px hsla(0, 0%, 0%, .35), 0 2px 0 hsla(0, 0%, 100%, .15);

// Setup
html {
  font-family: montserrat;
}

.demo {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: $color-background;
}

// Form Styling
::placeholder {
  color: hsla(0, 0, 100%, .6);
}

.form {
  display: flex;
  flex-direction: column;

  & label {
    color: #fff;
    letter-spacing: .15em;
    margin-bottom: -.75rem;
    font-weight: bold;
  }

  &__inset {
    border: none;
    background: $color-inset;
    box-shadow: $shadow-inset;
    width: 35rem;
    margin: 2rem 0;
    padding: 1rem .5rem;
    color: #fff;
  }
} """,
     "js": """ """,},
    
    {"html": """<div class="demo">
  <form class="form" action="submit">
    <label for="name">Subscribe Today!</label>
    <input class="form__inset" type="text" placeholder="Email" name="email">
  </form>
</div> """,
     "css": """// Variables
$color-background: hsl(224, 24%, 32%);
$color-inset: hsl(230, 22%, 27%);
$shadow-inset: inset 0 2px 2px hsla(0, 0%, 0%, .35), 0 2px 0 hsla(0, 0%, 100%, .15);

// Setup
html {
  font-family: montserrat;
}

.demo {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: $color-background;
}

// Form Styling
::placeholder {
  color: hsla(0, 0, 100%, .6);
}

.form {
  display: flex;
  flex-direction: column;

  & label {
    color: #fff;
    letter-spacing: .15em;
    margin-bottom: -.75rem;
    font-weight: bold;
  }

  &__inset {
    border: none;
    background: $color-inset;
    box-shadow: $shadow-inset;
    width: 35rem;
    margin: 2rem 0;
    padding: 1rem .5rem;
    color: #fff;
  }
} """,
     "js": """ """,},
    
    {"html": """<form>
	<label for="search">Search</label>
	<input id="search" type="search" pattern=".*\S.*" required>
	<span class="caret"></span>
</form> """,
     "css": """* {
	border: 0;
	box-sizing: border-box;
	margin: 0;
	padding: 0;
}
:root {
	--bg: #e3e4e8;
	--fg: #17181c;
	--input: #ffffff;
	--primary: #255ff4;
	--dur: 1s;
	font-size: calc(16px + (24 - 16)*(100vw - 320px)/(1280 - 320));
}
body, input {
	color: var(--fg);
	font: 1em/1.5 Hind, sans-serif;
}
body {
	background: var(--bg);
	display: flex;
	height: 100vh;
}
form, input, .caret {
	margin: auto;
}
form {
	position: relative;
	width: 100%;
	max-width: 17em;
}
input, .caret {
	display: block;
	transition: all calc(var(--dur) * 0.5) linear;
}
input {
	background: transparent;
	border-radius: 50%;
	box-shadow: 0 0 0 0.25em inset;
	caret-color: var(--primary);
	width: 2em;
	height: 2em;
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
}
input:focus, input:valid {
	background: var(--input);
	border-radius: 0.25em;
	box-shadow: none;
	padding: 0.75em 1em;
	transition-duration: calc(var(--dur) * 0.25);
	transition-delay: calc(var(--dur) * 0.25);
	width: 100%;
	height: 3em;
}
input:focus {
	animation: showCaret var(--dur) steps(1);
	outline: transparent;
}
input:focus + .caret, input:valid + .caret {
	animation: handleToCaret var(--dur) linear;
	background: transparent;
	width: 1px;
	height: 1.5em;
	transform: translate(0,-1em) rotate(-180deg) translate(7.5em,-0.25em);
}
input::-webkit-search-decoration {
	-webkit-appearance: none;
}
label {
	color: #e3e4e8;
	overflow: hidden;
	position: absolute;
	width: 0;
	height: 0;
}
.caret {
	background: currentColor;
	border-radius: 0 0 0.125em 0.125em;
	margin-bottom: -0.6em;
	width: 0.25em;
	height: 1em;
	transform: translate(0,-1em) rotate(-45deg) translate(0,0.875em);
	transform-origin: 50% 0;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {	
	:root {
		--bg: #17181c;
		--fg: #e3e4e8;
		--input: #2e3138;
		--primary: #5583f6;
	}
}

/* Animations */
@keyframes showCaret {
	from {
		caret-color: transparent;
	}
	to {
		caret-color: var(--primary);
	}
}
@keyframes handleToCaret {
	from {
		background: currentColor;
		width: 0.25em;
		height: 1em;
		transform: translate(0,-1em) rotate(-45deg) translate(0,0.875em);
	}
	25% {
		background: currentColor;
		width: 0.25em;
		height: 1em;
		transform: translate(0,-1em) rotate(-180deg) translate(0,0.875em);
	}
	50%, 62.5% {
		background: var(--primary);
		width: 1px;
		height: 1.5em;
		transform: translate(0,-1em) rotate(-180deg) translate(7.5em,2.5em);
	}
	75%, 99% {
		background: var(--primary);
		width: 1px;
		height: 1.5em;
		transform: translate(0,-1em) rotate(-180deg) translate(7.5em,-0.25em);
	}
	87.5% {
		background: var(--primary);
		width: 1px;
		height: 1.5em;
		transform: translate(0,-1em) rotate(-180deg) translate(7.5em,0.125em);
	}
	to {
		background: transparent;
		width: 1px;
		height: 1.5em;
		transform: translate(0,-1em) rotate(-180deg) translate(7.5em,-0.25em);
	}
} """,
     "js": """ """,},
    
    {"html": """<div class="container">
	<div class="panel">
		<div class="panel-header">
			<div class="panel-header-logo">
				<svg xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" xml:space="preserve" height="500" width="500" version="1.0" viewBox="0 0 5.5555557 5.5555555">
	<g transform="matrix(1.0755 0 0 1.0755 -3.5103 -1.6684)">
		<path fill="#3071cd" d="m5.8465 1.9131c0.57932 0 1.1068 0.222 1.5022 0.58547-0.1938-0.0052-0.3872 0.11-0.3952 0.3738-0.0163 0.5333 0.6377 0.6469 0.2853 1.7196l-0.2915 0.8873-0.7939-2.3386c-0.0123-0.0362 0.002-0.0568 0.0465-0.0568h0.22445c0.011665 0 0.021201-0.00996 0.021201-0.022158v-0.13294c0-0.012193-0.00956-0.022657-0.021201-0.022153-0.42505 0.018587-0.8476 0.018713-1.2676 0-0.0117-0.0005-0.0212 0.01-0.0212 0.0222v0.13294c0 0.012185 0.00954 0.022158 0.021201 0.022158h0.22568c0.050201 0 0.064256 0.016728 0.076091 0.049087l0.3262 0.8921-0.4907 1.4817-0.8066-2.3758c-0.01-0.0298 0.0021-0.0471 0.0308-0.0471h0.25715c0.011661 0 0.021197-0.00996 0.021197-0.022158v-0.13294c0-0.012193-0.00957-0.022764-0.021197-0.022153-0.2698 0.014331-0.54063 0.017213-0.79291 0.019803 0.39589-0.60984 1.0828-1.0134 1.8639-1.0134l-0.0000029-0.0000062zm1.9532 1.1633c0.17065 0.31441 0.26755 0.67464 0.26755 1.0574 0 0.84005-0.46675 1.5712-1.1549 1.9486l0.6926-1.9617c0.1073-0.3036 0.2069-0.7139 0.1947-1.0443h-0.000004zm-1.2097 3.1504c-0.2325 0.0827-0.4827 0.1278-0.7435 0.1278-0.2247 0-0.4415-0.0335-0.6459-0.0955l0.68415-1.9606 0.70524 1.9284v-1e-7zm-1.6938-0.0854c-0.75101-0.35617-1.2705-1.1213-1.2705-2.0075 0-0.32852 0.071465-0.64038 0.19955-0.92096l1.071 2.9285 0.000003-0.000003zm0.95023-4.4367c1.3413 0 2.4291 1.0878 2.4291 2.4291s-1.0878 2.4291-2.4291 2.4291-2.4291-1.0878-2.4291-2.4291 1.0878-2.4291 2.4291-2.4291zm0-0.15354c1.4261 0 2.5827 1.1566 2.5827 2.5827s-1.1566 2.5827-2.5827 2.5827-2.5827-1.1566-2.5827-2.5827 1.1566-2.5827 2.5827-2.5827z"/>
	</g>
</svg>
			</div>
			<h1 class="panel-header-title">Sign in
				<h1 />
				<p class="panel-header-info">Don't have a Wordpress account? <a href="#" class="link">Create an account</a></p>
		</div>
		<form class="form" action="javascript:void(0);">
			<div class="input">
				<label class="input-label">E-mail</label>
				<input type="email" class="input-field" />
			</div>
			<div class="input">
				<label class="input-label">Password</label>
				<input type="password" class="input-field" />
			</div>
			<div class="input">
				<button class="input-submit">Sign in</button>
			</div>
		</form>
		<div class="panel-footer">
			<p class="panel-footer-info">Forgot your username or password? <a href="#" class="link">Restore account</a></p>
		</div>
	</div>
</div> """,
     "css": """*, *:after, *:before {
	box-sizing: border-box;
}

:root {
	--primary-text-color: #043959;
	--primary-color: #3071cd;
	--secondary-color: #2e69cb;
}

:focus {
	outline: .125rem solid var(--primary-color);
	outline-offset: .125rem;
}

body {
	font-family: "Inter", sans-serif;
	color: var(--primary-text-color);
	line-height: 1.5;
	font-size: 1em;
}

// RESET
input, button {
	font: inherit;
	border-radius: 0;
	border: 0;
	background-color: transparent;
	box-shadow: none;
}
// END RESET 

.container {	
	display: flex;
	align-items: center;
	justify-content: center;
	min-height: 100vh;	
	background-image: linear-gradient(135deg, #52E5E7 5%, #130CB7 100%);
}

.panel {
	background-color: #FFF;
	max-width: 34rem;
	display: flex;
	flex-direction: column;
	padding: 4rem 3rem;
	border-radius: .5rem;
	box-shadow: .75rem .75rem 1.75rem 0 rgba(#000, .25);
}

.panel-header {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
}

.panel-header-logo {
	width: 5rem;
	height: 5rem;
	svg {
		max-width: 100%;	
		max-height: 100%;
	}
}

.panel-header-title {
	margin-top: 1.5rem;
	font-size: 1.75rem;
	font-weight: 700;
}

.panel-header-info {
	margin-top: 1rem;
	text-align: center;
}

.link {
	text-decoration: none;
	color: var(--primary-color);
	border-bottom: 0.0625rem solid;
	&:hover {
		color: var(--secondary-color);
	}
}

.form {
	margin-top: 2rem;
	display: flex;
	flex-direction: column;
}

.input {
	display: flex;
	flex-direction: column;
	& + .input {
		margin-top: 1.5rem;
	}
}

.input-label {
	font-weight: 600;
}

.input-field {
	margin-top: .25rem;
	border: 0.0625rem solid #999;
}

.input-submit {
	padding: 1rem;
	background-color: var(--primary-color);
	color: #FFF;
	&:hover {
		background-color: var(--secondary-color);
	}
}

.input-field, .input-submit {
	padding: .5rem .75rem;
	min-height: 3rem;
}

.panel-footer {
	display: flex;
	justify-content: center;
	margin-top: 1.5rem;
}

.panel-footer-info {
	text-align: center;
} """,
     "js": """ """,},
    
    {"html": """<h1>Input Animation</h1>
<div class="form">
  <input type="text" name="text" autocomplete="off" required />
  <label for="text" class="label-name">
    <span class="content-name">
      Your Text
    </span>
  </label>
</div> """,
     "css": """body {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: #f38181;
  font-family: "montserrat", sans-serif;
  font-weight: 500;
  color: #fff;
}
h1 {
  padding-bottom: 30px;
  font-weight: 900;
  font-size: 35px;
}
.form {
  width: 30%;
  position: relative;
  height: 60px;
  overflow: hidden;
}

.form input {
  width: 100%;
  height: 100%;
  color: #fff;
  padding-top: 20px;
  border: none;
  background-color: #f38181;
}
.form label {
  position: absolute;
  bottom: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  pointer-events: none;
  border-bottom: 1px solid white;
}
.form label::after {
  content: "";
  position: absolute;
  bottom: -1px;
  left: 0px;
  width: 100%;
  height: 100%;
  border-bottom: 3px solid #fce38a;
  transform: translateX(-100%);
  transition: all 0.3s ease;
}

.content-name {
  position: absolute;
  bottom: 0px;
  left: 0px;
  padding-bottom: 5px;
  transition: all 0.3s ease;
}
.form input:focus {
  outline: none;
}
.form input:focus + .label-name .content-name,
.form input:valid + .label-name .content-name {
  transform: translateY(-150%);
  font-size: 14px;
  left: 0px;
  color: #fce38a;
}
.form input:focus + .label-name::after,
.form input:valid + .label-name::after {
  transform: translateX(0%);
}
 """,
     "js": """ """,},
    
    {"html": """<!-- inspired by http://littlebigdetails.com/post/82478225432/circleci-once-activated-the-input-placeholders -->

<div class="input-wrapper">
  <input type="text" id="user" required>
  <label for="user">user name</label>
</div>
  
<div class="input-wrapper">
  <input type="password" required>
  <label for="user">password</label>
</div> """,
     "css": """@import "nib"

body
  padding:40px
  font-family:"Helvetica Neue"

.input-wrapper
  position:relative
  line-height:14px
  margin:0 10px
  display:inline-block

label
  color:#bbb
  font-size:11px
  text-transform:uppercase
  position:absolute
  z-index:2
  left:20px
  top:14px
  padding:0 2px
  pointer-events:none
  background:white
  transition:transform 100ms ease
  transform:translateY(-20px)

input 
  font-size:13px
  color:#555
  outline:none
  border:1px solid #bbb
  padding:10px 20px
  border-radius:20px
  position:relative

  &:invalid + label
    transform:translateY(0)
    
  &:focus
    border-color:#2b96f1

    & + label
      color:#2b96f1
      transform:translateY(-20px) """,
     "js": """ """,},
    
    {"html": """<div class = "con-input">
    <input placeholder = "User" type = "text">
    <i class = 'bx bx-user icon'></i>
    <div class = "bg"></div>
</div>
 """,
     "css": """.con-input{
  background: tan;
  display: flex;
  align-items: center;
  padding: 5px;
  border-radius:12px;
  position: relative;
  width:240px;
  left: 50%;
}
.con-input input{
  border:0px;
  background: transparent;
  outline: none;
  font-size:.9rem;
  font-family:'poppins', sans-serif;
  margin-left: 8px;
  width: 200px;
  transition: all .25s ease;
}
.con-input input:focus{
  padding-left: 5px;
  padding-right: 0px;
}
.con-input input:focus ~ .bg{
  border:2px solid #000;
}
.con-input input:focus ~ i{
  transform: translate(0,-8px);
  box-shadow: 0px 8px 20px 0px
    rgba(0,0,0,.15);
}
.con-input i.icon{
  order: -1;
  background: #fff;
  border-radius: 12px;
  display:flex;
  align-items:center;
  justify-content:center;
  width: 31px;
  height: 31px;
  z-index:20px;
  transition: all .25s ease;
}
.bg{
  background: transparent;
  width: 100%;
  height: 100%;
  position: absolute;
  z-index:1;
  left: 0px;
  top: 0px;
  pointer-events:none;
  border-radius: inherit;
  box-sizing: border-box;
  border:2px solid transparent;
  transition: all .25s ease;
} """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
    
    {"html": """ """,
     "css": """ """,
     "js": """ """,},
]