# ijkParameterPlotter
<h3>3D Parametric equation rendering in python turtle, designed for single runs in order to maximize performance.</h3>
<hr />
<img width="1879" height="1121" alt="image" src="https://github.com/user-attachments/assets/5f6f987c-55bc-47f4-9541-5d9ef440af30" />
</br>
 </br><blockquote>To adjust the ammount of rendering steps depending on your system, consult the last lines of code.</blockquote>
<h1>[ A P P E N D I X ]</h1>
<section>
    <h3>Presets</h3>
    <p>
      Basic modules/programs are listed on the <b>left</b>; preset parametric equations are on the <b>right</b>.
    </p>
    <blockquote>
      <b>Note on *[...] Differential Systems:</b> Presets marked with an <b>asterisk (*)</b> use <i>Ordinary Differential Equations (ODEs)</i>. These are pre-calculated for performance, allowing ~7,500 points to render smoothly. Avoid multi-value color modes (1, 2, 3, 7) here to maintain clarity.
    </blockquote>
  </section>



  <section>
    <h3>Visuals & Perspective</h3>
    <ul>
      <li><b>Camera:</b> Locked at <code>(0, 0, 0)</code> (Origin-centric).</li>
      <li><b>Scaling:</b> Moves the view closer (<code>+</code>) or further away (<code>-</code>).</li>
      <li><b>Eyes(x, z):</b> Controls the viewing angle.
        <ul>
          <li><code>-x</code>: Moves perspective up.</li>
          <li><code>z</code>: Moves perspective sideways.</li>
          <li><i>For 2D:</i> Set <code>eyes(x) = -90</code> and <code>eyes(z) = 0</code>.</li>
        </ul>
      </li>
      <li><b>Spin:</b> Rotates the camera at a <b>ratio of x:2z</b>. Because the vertical and horizontal speeds differ, the rotation is non-repeating.</li>
    </ul>
  </section>



  <section>
    <h3>Mathematical Inputs</h3>
    <h4>Standard Parametrics</h4>
    <p>Defined by <code>x(t)</code>, <code>y(t)</code>, and <code>z(t)</code>. For standard <b>2D Cartesian</b> functions:</p>
    <ul>
      <li><code>x(t) = t</code></li>
      <li><code>y(t) = e**t</code> (or any function of <i>t</i>)</li>
      <li><code>z(t) = 0</code></li>
    </ul>
    <h4>Domain & Performance</h4>
    <p><b>t(min) / t(max):</b> Defines the domain. Avoid excessive ranges (e.g., [0, 4π] for a circle) to keep rendering efficient.</p>
    <h4>Differential Systems: Initial Conditions</h4>
    <p>Standard starting points are <code>(~0.1, 0, 0)</code>. 
      <br>Do not use <code>(0, 0, 0)</code> as the math will reach an equilibrium and get stuck.
    </p>
  </section>



  <section>
    <h3>Special Modules</h3>
    <ul>
      <li><b>[OC] Oscilloscope:</b> 
        <ul>
          <li>Frequency (<i>f</i>): To get a constant <i>k=1</i>, use <code>0.15915</code> (1/2π).</li>
          <li><b>Time per Division:</b> Controls scrolling speed. Values ≤ <code>0.3</code> are recommended.</li>
        </ul>
      </li>
    </ul>
  </section>
<hr />
<img width="649" height="931" alt="image" src="https://github.com/user-attachments/assets/7db3a4f6-a1d0-444b-92af-52f00d920e3d" />
<p> - The main menu, with a chosen module.</p>
<hr />
<img width="1827" height="1197" alt="image" src="https://github.com/user-attachments/assets/85c4d80e-d5d5-4e74-b387-1eb92981dc90" />
<hr />
<img width="1881" height="1125" alt="image" src="https://github.com/user-attachments/assets/1e5cadef-01b1-4c82-a37a-434b2c48d2b4" />
 - Static image of the oscilloscope, still containing the appendix which has now been moved to the README.md for comfort.
<hr />
<img width="1883" height="1122" alt="image" src="https://github.com/user-attachments/assets/91cca120-c054-4d4c-8d4d-800669781eb1" />
 - Static image of the [SR] SpinningRose preset with color gradient [2] Red -> Blue
