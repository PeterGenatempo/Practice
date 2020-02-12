//
//  ViewController.swift
//  SampleApp
//
//  Created by Peter Genatempo on 7/2/18.
//  Copyright © 2018 Peter Genatempo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var currentMoney:Double = 0;
    
    var tapMultiplier:Double = 100;
    
    var nextUpgradeMultiplier:Double = 1.25;
    
    var upgrade1Cost:Double = 10;
    var upgrade2Cost:Double = 100;
    var upgrade3Cost:Double = 1000;
    var upgrade4Cost:Double = 10000;
    var upgrade5Cost:Double = 100000;
    
    var upgrade1Addition:Double = 1;
    var moneyPerSec2:Double = 1;
    var moneyPerSec3:Double = 10;
    var moneyPerSec4:Double = 100;
    var moneyPerSec5:Double = 1000;
    
    var moneyPerSec:Double = 0;
    
    var gameTimer: Timer?
    
    @IBOutlet weak var moneyLabel: UILabel!
    
    @IBOutlet weak var perSecLabel: UILabel!
    
    @IBOutlet weak var upgrade1: UILabel!
    
    @IBOutlet weak var upgrade2: UILabel!
    
    @IBOutlet weak var upgrade3: UILabel!
    
    @IBOutlet weak var upgrade4: UILabel!
    
    @IBOutlet weak var upgrade5: UILabel!
    
    @IBAction func tapButton(_ sender: UIButton) {
        if sender.tag == 1 {
            currentMoney = currentMoney + (1 * tapMultiplier).rounded();
            moneyLabel.text = "$" + String(currentMoney);
        }
    }
    
    @objc func updateClock() {
        currentMoney = currentMoney + moneyPerSec;
        currentMoney = currentMoney + (1 * tapMultiplier).rounded();
        moneyLabel.text = "$" + String(currentMoney);
    }
    
    @IBAction func upgradeButtons(_ sender: UIButton) {
        if sender.tag == 2 && currentMoney >= upgrade1Cost {
            currentMoney = (currentMoney - upgrade1Cost).rounded();
            moneyLabel.text = "$" + String(currentMoney);
            tapMultiplier = tapMultiplier + upgrade1Addition;
            upgrade1Cost = (upgrade1Cost * nextUpgradeMultiplier).rounded();
            upgrade1.text = "$" + String(upgrade1Cost);
        }else if sender.tag == 3 && currentMoney >= upgrade2Cost {
            currentMoney = (currentMoney - upgrade2Cost).rounded();
            moneyLabel.text = "$" + String(currentMoney);
            upgrade2Cost = (upgrade2Cost * nextUpgradeMultiplier).rounded();
            upgrade2.text = "$" + String(upgrade2Cost);
            moneyPerSec = moneyPerSec + moneyPerSec2;
            perSecLabel.text = "$" + String(moneyPerSec) + "/s";
        }else if sender.tag == 4 && currentMoney >= upgrade3Cost {
            currentMoney = (currentMoney - upgrade3Cost).rounded();
            moneyLabel.text = "$" + String(currentMoney);
            upgrade3Cost = (upgrade3Cost * nextUpgradeMultiplier).rounded();
            upgrade3.text = "$" + String(upgrade3Cost);
            moneyPerSec = moneyPerSec + moneyPerSec3;
            perSecLabel.text = "$" + String(moneyPerSec) + "/s";
        }else if sender.tag == 5 && currentMoney >= upgrade4Cost {
            currentMoney = (currentMoney - upgrade4Cost).rounded();
            moneyLabel.text = "$" + String(currentMoney);
            upgrade4Cost = (upgrade4Cost * nextUpgradeMultiplier).rounded();
            upgrade4.text = "$" + String(upgrade4Cost);
            moneyPerSec = moneyPerSec + moneyPerSec4;
            perSecLabel.text = "$" + String(moneyPerSec) + "/s";
        }else if sender.tag == 6 && currentMoney >= upgrade5Cost {
            currentMoney = (currentMoney - upgrade5Cost).rounded();
            moneyLabel.text = "$" + String(currentMoney);
            upgrade5Cost = (upgrade5Cost * nextUpgradeMultiplier).rounded();
            upgrade5.text = "$" + String(upgrade5Cost);
            moneyPerSec = moneyPerSec + moneyPerSec5;
            perSecLabel.text = "$" + String(moneyPerSec) + "/s";
        }
            
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        gameTimer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(updateClock), userInfo: nil, repeats: true)
    }
}
