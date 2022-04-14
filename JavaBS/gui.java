package threads_p05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class gui extends JFrame{
	private JPanel contentPane;
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					gui frame = new gui();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	public gui() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(500,500,500,500);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		
		JLabel lblNewLabel = new JLabel(new ImageIcon("dude/0.gif"));
		thread newthread =  new thread(lblNewLabel,this);
		newthread.SetFolder("dude", 11);
		newthread.SetAxis(0);
		newthread.start();
		JLabel lblNewLabel2 = new JLabel(new ImageIcon("bat/0.gif"));
		thread newthread2 =  new thread(lblNewLabel2,this);
		newthread2.SetFolder("bat", 24);
		newthread2.SetAxis(1);
		newthread2.start();
		JLabel lblNewLabel3 = new JLabel(new ImageIcon("fart/0.gif"));
		thread newthread3 =  new thread(lblNewLabel3,this);
		newthread3.SetFolder("fart", 5);
		newthread3.SetAxis(3);
		newthread3.start();
		JLabel lblNewLabel4 = new JLabel(new ImageIcon("jake/0.gif"));
		thread newthread4 =  new thread(lblNewLabel4,this);
		newthread4.SetFolder("jake", 31);
		newthread4.SetAxis(3);
		newthread4.start();
		JLabel lblNewLabel5 = new JLabel(new ImageIcon("tony/0.gif"));
		thread newthread5 =  new thread(lblNewLabel5,this);
		newthread5.SetFolder("tony", 2);
		newthread5.SetAxis(2);
		newthread5.start();

		contentPane.add(lblNewLabel, BorderLayout.EAST);
		contentPane.add(lblNewLabel2,BorderLayout.WEST);
		contentPane.add(lblNewLabel3,BorderLayout.NORTH);
		contentPane.add(lblNewLabel4,BorderLayout.SOUTH);
		contentPane.add(lblNewLabel5,BorderLayout.CENTER);
	}
}