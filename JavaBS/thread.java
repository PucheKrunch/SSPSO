package threads_p05;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JFrame;

public class thread extends Thread implements KeyListener{
	private JLabel _labelgif;
	private ImageIcon img;
	private String folder;
	private int size;
	private JFrame frame;
	private boolean movement;
	private int key;
	//0 y, 1 x, 3 NO SE MUEVE
	private int axis;
	public thread() {
		// TODO Auto-generated constructor stub
	}

	public thread(JLabel labelgif, JFrame frame) {
		super();
		_labelgif = labelgif;
		this.frame = frame;
		this.frame.addKeyListener(this);
	}
	public void SetFolder(String folder, int size) {
		this.folder = folder;
		this.size = size;
	}
	public String GetFolder() {
		return this.folder;
	}
	public int GetSize() {
		return this.size;
	}
	public void SetAxis(int axis) {
		this.axis = axis;
	}
	public int GetAxis() {
		return this.axis;
	}
	public boolean GetMovement() {
		return this.movement;
	}
	public int GetKey() {
		return this.key;
	}
	public void run () {
		axis = this.GetAxis();
		int i= 0;
		boolean flag = true;
		while (true) {
				if(axis==3) {
					img = new ImageIcon(this.GetFolder()+"/"+i+".gif");
					_labelgif.setIcon(img);
				}
				else if(axis != 2){
					img = new ImageIcon(this.GetFolder()+"/"+i+".gif");
					_labelgif.setIcon(img);
					if(axis == 1) {
						if(_labelgif.getLocation().x > 220 && _labelgif.getLocation().x < 260) {
							flag = false;
						}
						if(_labelgif.getLocation().x >= 0 && _labelgif.getLocation().x < 20) {
							flag = true;
						}
						if(flag) {
							_labelgif.setLocation(_labelgif.getLocation().x+10,_labelgif.getLocation().y);	
						}
						
						else {
							_labelgif.setLocation(_labelgif.getLocation().x-10,_labelgif.getLocation().y);
						}
					}
					else {
						if(_labelgif.getLocation().y > 420 && _labelgif.getLocation().y < 460) {
							flag = false;
						}
						if(_labelgif.getLocation().y > 200 && _labelgif.getLocation().y < 220) {
							flag = true;
						}
						if(flag) {
							_labelgif.setLocation(_labelgif.getLocation().x,_labelgif.getLocation().y+10);
						}
						else {
							_labelgif.setLocation(_labelgif.getLocation().x,_labelgif.getLocation().y-10);
						}
					}
				}
				else {
					img = new ImageIcon(this.GetFolder()+"/"+i+".gif");
					_labelgif.setIcon(img);
					if (this.GetMovement()) {
						if (this.GetKey() == 38) {
							_labelgif.setLocation(_labelgif.getLocation().x,_labelgif.getLocation().y-10);
						}
						else if (this.GetKey() == 40) {
							_labelgif.setLocation(_labelgif.getLocation().x,_labelgif.getLocation().y+10);
						}
						else if (this.GetKey() == 37) {
							_labelgif.setLocation(_labelgif.getLocation().x-10,_labelgif.getLocation().y);
						}
						else if (this.GetKey() == 39) {
							_labelgif.setLocation(_labelgif.getLocation().x+10,_labelgif.getLocation().y);
						}
					}
				}
				
				i++;
				if(i== this.GetSize())
					i=0;
				try {
					Thread.sleep(100);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
		}
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
	}

	@Override
	public void keyPressed(KeyEvent e) {
		// TODO Auto-generated method stub
		this.movement = true;
		this.key = e.getKeyCode();
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		this.movement = false;
	}
}
